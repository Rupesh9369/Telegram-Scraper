import csv
import os
import sys
import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

def load_config():
    """Load configuration from file."""
    if not os.path.exists('config.txt'):
        print("Configuration file not found. Please run setup.py first.")
        sys.exit(1)
    
    config_dict = {}
    with open('config.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:
                continue  # Skip empty lines or lines without '='
            key, value = line.split('=', 1)
            config_dict[key.strip()] = value.strip()
    
    return config_dict

def get_group_link():
    """Retrieve the group link from user input."""
    group_link = input("Enter your own group link (e.g., https://t.me/joinchat/XXXXXXX): ").strip()
    if not group_link:
        print("Group link cannot be empty.")
        sys.exit(1)
    return group_link

def get_csv_file_path():
    """Retrieve the path to the CSV file from user input."""
    file_path = input("Enter the path to members.csv file: ").strip()
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        sys.exit(1)
    return file_path

def read_members(file_path, limit=50):
    """Read members from CSV file and return the first 'limit' members."""
    members = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Username'] and row['First Name']:
                members.append(row)
                if len(members) == limit:
                    break
    return members

def remove_added_members(file_path, added_members):
    """Remove added members from the CSV file."""
    temp_file = file_path + '.temp'
    added_ids = set(member['ID'] for member in added_members)

    with open(file_path, 'r', encoding='utf-8') as infile, \
         open(temp_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row['ID'] not in added_ids:
                writer.writerow(row)

    os.replace(temp_file, file_path)

async def main():
    # Load configuration
    config = load_config()
    app_id = config.get('app_id')
    api_hash = config.get('api_hash')

    # Initialize the client
    client = TelegramClient('session', int(app_id), api_hash)
    await client.connect()

    if not await client.is_user_authorized():
        print("You are not authorized. Please run setup.py to log in.")
        await client.disconnect()
        sys.exit(1)

    # Get group link and CSV file path from user
    group_link = get_group_link()
    csv_file_path = get_csv_file_path()

    # Extract the group entity from the link
    try:
        entity = await client.get_entity(group_link)
    except Exception as e:
        print(f"Error fetching group: {e}")
        await client.disconnect()
        sys.exit(1)

    # Read 50 members from the CSV
    members_to_add = read_members(csv_file_path, 50)

    if not members_to_add:
        print("No valid members found in the CSV file.")
        await client.disconnect()
        sys.exit(1)

    # Add members to the group
    added_members = []
    try:
        user_ids = [int(member['ID']) for member in members_to_add]
        await client(InviteToChannelRequest(
            channel=entity,
            users=user_ids
        ))
        added_members = members_to_add
        print(f"Added {len(added_members)} members.")
    except Exception as e:
        print(f"Error adding members: {e}")

    # Remove added members from the CSV file
    if added_members:
        remove_added_members(csv_file_path, added_members)
        print(f"Removed {len(added_members)} added members from {csv_file_path}")
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())