from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from livvy import livvycmd
from pyrogram import filters 
from livvy import help_message
from time import time
from datetime import datetime
from config import BOT_NAME, BOT_USERNAME


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



@livvycmd.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(_,message):
    chat_type = message.chat.type
    if chat_type == "private":
        current_time = datetime.utcnow()
        uptime_sec = (current_time - START_TIME).total_seconds()
        uptime = await _human_time_duration(int(uptime_sec))
    
    await message.reply_photo(
        photo=f"https://telegra.ph/file/53115c567caf7350794dc.jpg",
        caption=f"""Hey🤞, I am {BOT_NAME}.
I am an Advanced Group Manager Bot, With Lots of Cool Features❤️.

Build With Python and Pyrogram.
**Uptime** : `{uptime}` """,
        reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton('Add Me Now' , url="https://t.me/MissLivvyBot?groupstart=true")],
            [InlineKeyboardButton('Need Help?' , callback_data="help")]
        ]))
    elif chat_type in ["group", "supergroup"]:
        await message.reply_photo(
            photo=f"https://telegra.ph/file/53115c567caf7350794dc.jpg",
            caption=f"""Thanks For Adding Me.
I am an Advanced Group Manager Bot, With Lots of Cool Features❤️.
