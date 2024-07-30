import csv
import os
import sys
import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

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
    """Retrieve the group link from a file."""
    if not os.path.exists('group_link.txt'):
        print("Group link file not found. Please create 'group_link.txt' with the default group link.")
        sys.exit(1)
    
    with open('group_link.txt', 'r') as f:
        link = f.read().strip()
    
    return link

async def main():
    # Load configuration
    config = load_config()
    phone_number = config.get('phone_number')
    app_id = config.get('app_id')
    api_hash = config.get('api_hash')

    # Initialize the client
    client = TelegramClient('session', int(app_id), api_hash)
    await client.connect()

    if not await client.is_user_authorized():
        print("You are not authorized. Please run setup.py to log in.")
        await client.disconnect()
        sys.exit(1)

    # Get the default group link
    group_link = get_group_link()

    # Extract the group username or ID from the link
    try:
        entity = await client.get_entity(group_link)
    except Exception as e:
        print(f"Error fetching group: {e}")
        await client.disconnect()
        sys.exit(1)

    # Fetch group participants
    participants = []
    try:
        offset = 0
        limit = 100
        while True:
            result = await client(GetParticipantsRequest(
                channel=entity,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0
            ))
            if not result.users:
                break
            participants.extend(result.users)
            offset += len(result.users)
    except Exception as e:
        print(f"Error fetching participants: {e}")
        await client.disconnect()
        sys.exit(1)
    
    # Write participants to CSV
    with open('members.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'Username', 'First Name', 'Last Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user in participants:
            writer.writerow({
                'ID': user.id,
                'Username': user.username if user.username else '',
                'First Name': user.first_name if user.first_name else '',
                'Last Name': user.last_name if user.last_name else ''
            })
    
    print(f"Members have been successfully saved to 'members.csv'.")
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())