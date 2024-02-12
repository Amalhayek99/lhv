


from telebot import types
from config import BOT_TOKEN
from database import find_document_by_md5
from decrypt import brute_force_decrypt
import telebot
import os  # Import the os module

bot = telebot.TeleBot(BOT_TOKEN)
user_state = {}

# Define states
(START, AWAITING_MD5, AWAITING_FILE, FILE_UPLOADED) = range(4)

def set_user_state(user_id, state):
    user_state[user_id] = state

def get_user_state(user_id):
    return user_state.get(user_id, START)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    button1 = types.KeyboardButton('MD5 Decryption')
    button2 = types.KeyboardButton('Encrypt File/Folder')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Welcome! Choose an option:", reply_markup=markup)
    set_user_state(message.chat.id, START)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == START and message.text == 'MD5 Decryption')
def handle_md5_decryption_request(message):
    bot.send_message(message.chat.id, "Please enter the MD5 hash:")
    set_user_state(message.chat.id, AWAITING_MD5)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == AWAITING_MD5)
def handle_md5_decryption(message):
    md5_hash = message.text.strip()
    document = find_document_by_md5(md5_hash)
    if document:
        name = document.get('name', 'Name not found')
        bot.send_message(message.chat.id, f"The name associated with the MD5 hash {md5_hash} is: {name}")
    else:
        bot.send_message(message.chat.id, "No data found for the provided MD5")
    set_user_state(message.chat.id, START)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == START and message.text == 'Encrypt File/Folder')
def handle_encrypt_file_folder_request(message):
    bot.send_message(message.chat.id, "Please upload your file/folder.")
    set_user_state(message.chat.id, AWAITING_FILE)

@bot.message_handler(content_types=['document'], func=lambda message: get_user_state(message.chat.id) == AWAITING_FILE)
def handle_file_upload(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = file_info.file_path.split('/')[-1]

    # Save the uploaded file to disk
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    print(f"File saved as: {file_name}")  # Print the file path

    # Attempt brute force decryption
    password = brute_force_decrypt(file_name)
    print(f"Brute force decryption result: {password}")  # Print the result of decryption

    if password != "Password not found.":
        bot.send_message(message.chat.id, f"The correct password is: {password}")
    else:
        bot.send_message(message.chat.id, "Failed to decrypt the file. Password not found.")

    set_user_state(message.chat.id, START)

bot.polling(none_stop=True)
