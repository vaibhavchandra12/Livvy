from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from livvy import bot
from pyrogram import filters 
from livvy import help_message
from time import time
from datetime import datetime
from config import BOT_NAME


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)



@bot.on_message(filters.command('start'))
async def start(_,message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/53115c567caf7350794dc.jpg",
        caption=f"""Hey🤞, I am {BOT_NAME}.
I am an Advanced Group Manager Bot, With Lots of Cool Features❤️.

Build With Python and Pyrogram.
**Uptime** : `{uptime}` """, reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('Need Help?' , callback_data="help")]
    ]))
