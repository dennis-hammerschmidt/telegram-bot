import sys
import os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import telegram
import random

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = <ADD_YOUR_CHAT_ID>

def send_photo(event, context):
    bot = telegram.Bot(token=TOKEN)
    photo_url = '<PATH_TO_IMAGES>/'
    rand_photo = random.choice(os.listdir(photo_url))
    with open(os.path.join(photo_url, rand_photo), 'rb') as file:
        bot.sendPhoto(chat_id = CHAT_ID, photo = file)
