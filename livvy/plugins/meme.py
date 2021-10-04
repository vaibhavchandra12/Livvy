from pyrogram import InlineKeyboardButton
from pyrogram import InlineKeyboardMarkup
from livvy import bot
from pyrogram import filters
import requests
from livvy import help_message 
from livvy.plugins.helpers import call_back_in_filter


@bot.on_callback_query(call_back_in_filter('meme'))
def callback_meme(_,query):
    if query.data.split(":")[1] == "next":
        query.message.delete()
        res = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
        img = res['image']
        title = res['title']
        bot.send_photo(query.message.chat.id , img , caption=title , reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Next" , callback_data="meme:next")],
        ]))



@bot.on_message(filters.command('rmeme'))
def rmeme(_,message):
    res = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
    img = res['image']
    title = res['title']
    bot.send_photo(message.chat.id , img , caption=title , reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Next" , callback_data="meme:next")]
    ]))


help_message.append(
    {
        "Module_Name": "Meme",
        "Help": "/rmeme - to get random memes from reddit"
    }
)
