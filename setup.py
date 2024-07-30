import os
import asyncio
from telethon.sync import TelegramClient

async def main():
    # User inputs for Telegram credentials
    
    # phone_number = input("Enter your phone number with country code (e.g., +1234567890): ")
    phone_number = "ENTER-MOBILE-NUMBER-WITH-COUNTRY-CODE"
    # app_id = input("Enter your App ID: ")
    app_id = "ENTER-APP-ID"
    # api_hash = input("Enter your API Hash: ")
    api_hash = "ENTER-API-HASH-KEY"

    # Create or update the configuration file
    with open('config.txt', 'w') as f:
        f.write(f"phone_number={phone_number}\n")
        f.write(f"app_id={app_id}\n")
        f.write(f"api_hash={api_hash}\n")

    print("Configuration file 'config.txt' created successfully.")

    # Initialize the client
    client = TelegramClient('session', int(app_id), api_hash)

    # Connect to the client
    await client.connect()

    # Check if the user is authorized
    if await client.is_user_authorized():
        print("You are already authorized.")
    else:
        # If not authorized, send the code
        await client.send_code_request(phone_number)
        code = input("Enter the code you received: ")
        await client.sign_in(phone_number, code)

        # Confirm successful login
        print("You are now logged in.")

    await client.disconnect()

if __name__ == "__main__":
    # Run the asynchronous main function
    asyncio.run(main())
