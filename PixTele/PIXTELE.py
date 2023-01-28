import telebot
import requests
import json
import random


bot = telebot.TeleBot("Enter Your Telegram token here!")


# URL of website with welcome images
welcome_images_url = "https://picsum.photos/v2/list?page=2&limit=100"

# Get list of welcome images from website
response = requests.get(welcome_images_url)
welcome_images = json.loads(response.text)

@bot.message_handler(commands=['start'])
def start_message(message):
    # Send random welcome image
    image_url = random.choice(welcome_images)['download_url']
    bot.send_photo(message.chat.id, image_url)
    bot.send_message(message.chat.id, f'Welcome! This bot was created by Aseel')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Commands: start, help, info, status')

@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id, 'This is a simple bot.')

@bot.message_handler(commands=['status'])
def status_message(message):
    bot.send_message(message.chat.id, 'Online.')

if __name__ == '__main__':
    bot.polling()
