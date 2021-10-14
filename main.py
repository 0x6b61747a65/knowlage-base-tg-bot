import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import message, user
from aiogram.types.message import Message
from user_db import authenticated_users as au

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

# stub on access for dev period
# my_username = os.getenv('TG_USERNAME')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if  message.from_user.username != au.username_in_db_exists(message.from_user.username):
        return await message.reply('Sorry, no access to you my friend!')
    else:
        with open('assets/bot_userpic.jpg', 'rb') as photo:
            """
            This handler will be called when user sends `/start` or `/help` command
            """
            await message.reply_photo(photo, caption="Hi!\nI'm your librarian for your Knowlage database!\nHow can I help you, mister?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    # skip_updates - no reply for messages sent when bot was offline
