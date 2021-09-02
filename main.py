# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad) (@BXBotz)

import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Glitch-Art-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """
Hai {}, 

I am a photo to glitch art telegram bot. Send me any photo I will convert photo to glitch art

<b>Made With ❤ By @m2botz</b>
"""

START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Updates Channel', url='https://t.me/m2botz'),
        InlineKeyboardButton('Support Group', url='https://t.me/m2botzsupport')
    ],
    [
        InlineKeyboardButton('Creator', url='https://t.me/ask_admin01')
    ]]
)

SOURCE_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Creator ', url='https://t.me/ask_admin01')
    ]]
)

PATH = os.environ.get("PATH", "./DOWNLOADS")

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["source"]))
async def source(bot, update):
    await update.reply_text(
        text=SOURCE_TEXT,
        reply_markup=SOURCE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.photo)
async def glitch_art(bot, update):
    download_path = PATH + "/" + str(update.from_user.id) + "/"
    download_location = download_path + "photo.jpg"
    message = await update.reply_text(
        text="`Processing...`",
        quote=True
    )
    try:
        await update.download(
            file_name=download_location
        )
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\n\nContact My [Support Group](https://t.me/m2botzsupport) "
        )
        return 
    await message.edit_text(
        text="`🎨 Converting to glitch...`"
    )
    try:
        glitch_art = glitchart.jpeg(download_location)
        await update.reply_photo(photo=glitch_art, quote=True)
        os.remove(download_location)
        os.remove(glitch_art)
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\n\nContact My [Support Group](https://t.me/m2botzsupport)"
        )
        return
    await message.delete()


Bot.run()
