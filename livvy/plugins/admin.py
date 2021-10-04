from re import escape
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message
from livvy import bot

from pyrogram import filters

from livvy import help_message



help_message.append({
    "Module_Name": "Admin" ,
    "Help": """
/ban - reply to a user
/unban user id or username
/pin - reply to a message
/unpin - reply to a message
/zombies - Kick Deleted Accounts
"""})
