from re import escape
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message
from livvy import bot
from livvy.plugins.helpers import call_back_in_filter 

from pyrogram import filters
from livvy import help_message

import asyncio
from typing import ClassVar, Optional

from pyrogram.errors import (
    ChatAdminRequired,
    FloodWait,
    UserAdminInvalid,
    UserIdInvalid,
)
from pyrogram.types import Chat, User


def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        if user_data.status == 'administrator' or user_data.status == 'creator':
            # print(f'is admin user_data : {user_data}')
            return True
        else:
            # print('Not admin')
            return False
    except:
        # print('Not admin')
        return False

        from pyrogram import filters 

class Admins(plugin.Plugin):
    name: ClassVar[str] = "Admins"
    helpable: ClassVar[bool] = True

        
@bot.on_callback_query(call_back_in_filter("admin"))
def admeme_callback(_,query):
    scammer = query.data.split(":")[2]
    if is_admin(query.message.chat.id , query.from_user.id) and query.data.split(":")[1] == "unban":
        bot.unban_chat_member(query.message.chat.id , scammer)
        query.answer('Unbanned!')
        query.message.edit(f'Unbanned [{scammer}](tg://user?id={scammer})' , parse_mode='markdown')
    else:
        message.reply('You are not admin!')

@bot.on_message(filters.command('ban') & filters.command(f'ban@MissLivvyBot'))
def ban(_,message):
    # scammer = reply.from_user.id
    reply = message.reply_to_message
    if is_admin(message.chat.id , message.from_user.id) and reply:
        bot.kick_chat_member(message.chat.id , message.reply_to_message.from_user.id)
        bot.send_message(message.chat.id ,f"Banned! {reply.from_user.username}" , parse_mode="markdown" ,reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Unban" , callback_data=f"admin:unban:{message.reply_to_message.from_user.id}")],
        ]))
    elif reply.from_user.id == 1971361970:
        message.reply('This Person is my owner!')
    else:
        message.reply('You are not admin')


@bot.on_message(filters.command('unban') & filters.command(f'unban@MissLivvyBot'))
def unban(_,message):
    try:
        user = message.text.split(" ")[1]
        if is_admin(message.chat.id , message.from_user.id):
            bot.unban_chat_member(message.chat.id , user)
            message.reply('Unbanned!')
    except Exception as e:
        message.reply(e)

    
@bot.on_message(filters.command('pin') & filters.command(f'pin@MissLivvyBotBot'))
def pin(_,message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        if is_admin(message.chat.id , message.from_user.id): 
            bot.pin_chat_message(message.chat.id , message_id)
    
    elif not is_admin(message.chat.id , message.from_user.id): 
        message.reply("You're not admin")
    else:
        message.reply('Reply to a message')


@bot.on_message(filters.command('unpin') & filters.command(f'unpin@DMissLivvyBotBot'))
def pin(_,message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        if is_admin(message.chat.id , message.from_user.id): 
            bot.unpin_chat_message(message.chat.id , message_id)
    
    elif not is_admin(message.chat.id , message.from_user.id): 
        message.reply("You're not admin")
    else:
        message.reply('Reply to a message')
        
@bot.on_message(filters.command('zombies') & filters.command(f'zombies@DMissLivvyBotBot'))
async def pin(_,message):
        chat = ctx.msg.chat
        zombie = 0

        await ctx.respond(await message.reply("Finding zombies account..."))
        async for member in self.bot.client.iter_chat_members(chat.id):  # type: ignore
            if member.user.is_deleted:
                zombie += 1
                try:
                    await self.bot.client.kick_chat_member(chat.id, member.user.id)
                except UserAdminInvalid:
                    zombie -= 1
                except FloodWait as flood:
                    await asyncio.sleep(flood.x)  # type: ignore

        if zombie == 0:
            return await message.reply("Zombies not found, group is clean..`")

        return await message.reply("**{}** `zombies found and has been removed..!` 🚮", zombie)

help_message.append({
    "Module_Name": "Admin" ,
    "Help": """
/ban - reply to a user
/unban user id or username
/pin - reply to a message
/unpin - reply to a message
/zombies - Kick Deleted Accounts
"""})
