import re
import logging
import asyncio
from pyrogram import Client, Filters
from telethon.tl.functions.users import GetFullUserRequest
from config import *

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

forwarded_files = set()

@app.on_message(Filters.command("start"))
def start(client, message):
    message.reply_text("I'm a Files/Video/Documents - Text Forward bot !!")

@app.on_message(filters.chat(FROM_CHANNEL))
async def forward_files(client, message):
    try:
        if message.media or message.text:
            if message.media:
                original_name = message.document.file_name if message.document else message.video.file_name if message.video else message.audio.file_name if message.audio else "Unknown"
                cleaned_name = re.sub(r'[-_+=?:;\'"{\}\[\]\\\/()]+', ' ', original_name)
                cleaned_name = re.sub(r'\.\w+', '', cleaned_name)

                caption = f"<b>{cleaned_name}</b>\n\nUploaded Here : @FSearch2bot"
                await app.send_message(TO_CHANNEL_ID, caption, parse_mode='html')

            elif message.text:
                await app.send_message(TO_CHANNEL_ID, message.text, link_preview=False, parse_mode='html')
    except Exception as e:
        print(f"Error: {e}")
        print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")

print("Bot has started.")
app.run_until_disconnected()

