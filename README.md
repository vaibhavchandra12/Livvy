Example for making new plugins

```
from nksama import bot , help_message
from pyrogram import filters

@bot.on_message(filters.command('hi'))
def hi(_,message):
  message.reply('hi')
  
help_message.append({"Module_Name": "hi" , "Help": "/hi - says hi"})

```
