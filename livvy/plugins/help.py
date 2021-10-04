from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup 
from livvy import bot, help_message

@bot.on_message(filters.command('help'))
def bothelp(_,message):
    keyboard = []
    for x in help_message:
        # keyboard = [(
        #     [InlineKeyboardButton(x['Module_Name'], callback_data=f"help:{x['Module_Name']}")],
        # )]
        keyboard.append([InlineKeyboardButton(f"{x['Module_Name']}" , callback_data=f"help:{x['Module_Name']}")])
        

    bot.send_message(message.chat.id , "Help And CMDs" , reply_markup=InlineKeyboardMarkup(keyboard))
