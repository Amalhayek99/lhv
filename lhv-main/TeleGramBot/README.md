# TelegramBot

To provide clear instructions for someone to run the project on their own laptop, you can follow these steps:

Install MongoDB: Download and install MongoDB from the official website if you haven't already. Follow the installation instructions provided for your operating system.

Import Database: Use the provided JSON file to import the necessary data into your MongoDB instance. This will set up the required database structure for the project.
The json file called : "HashedWords.json"

Generate Telegram Bot Token: Create a new bot on Telegram using BotFather. Follow the steps to create a new bot and obtain its API token.

Set Up Environment Variables: Copy your BotToken and store the Telegram bot token in the .env file (replace the key i have inserted)

Run the Bot Script: Execute the bot.py file to start the Telegram bot. This script is the main entry point for the bot and connects all the functionalities together.
Command : python bot.py (make sure ur terminal in the same directory of the file)

Interact with the Bot: Once the bot is running, open Telegram and search for your bot's username. Start a chat with the bot by sending /start or /help. The bot should respond with options to choose between MD5 and encrypted file functionalities.

Use MD5 Functionality: If you choose the MD5 functionality, the bot will prompt you to input a hashed text. Enter the hashed text, and the bot will search the database for a match and return the corresponding value.

Use Encrypted File Functionality: If you choose the encrypted file functionality, the bot will prompt you to upload an encrypted ZIP file. Upload the file, and the bot will perform a brute force attack to guess the password. Once the correct password is found, the bot will provide it and save the decrypted file in the same directory as bot.py.

With these steps, users should be able to set up and run the project on their own laptop, utilizing their own MongoDB instance and Telegram bot token.
