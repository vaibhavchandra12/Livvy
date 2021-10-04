from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from livvy import bot
from pyrogram import filters 
from livvy import help_message
from time import time
from datetime import datetime


@bot.on_message(filters.command('start'))
def start(_,message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9a50a0dbbac3e68f0cb3d.mp4",
        caption=f"""Hey🤞, I am {BOT_NAME}.
I am an Advanced Group Manager Bot, With Lots of Cool Featues❤️.

Build With Python and Pyrogram.
**Uptime** : `{uptime}` """, reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('help' , callback_data="help")]
    ]))
