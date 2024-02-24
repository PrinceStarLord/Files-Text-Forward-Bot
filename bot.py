import re
import logging
import asyncio
from pyrogram import Client, filters
from config import *

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

TO_CHANNEL_ID = -1001843660143
FROM_CHANNEL = -1001225782985

forwarded_files = set()

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("I'm a Files/Video/Documents - Text Forward bot !!")
@app.on_message(filters.chat(FROM_CHANNEL))
async def forward_message(client, message):
    try:
        # Check if the message is not from a private chat and not a poll
        if not message.chat.type == "private" and not message.poll:
            # Check if the message contains media
            if message.photo:
                photo = message.photo
                await app.send_photo(chat_id=TO_CHANNEL_ID, photo=photo.file_id, caption=message.text, disable_notification=True)
            elif message.document or message.web_page:
                await app.send_document(chat_id=TO_CHANNEL_ID, document=message.document.file_id, caption=message.text, disable_notification=True)
            else:
                # Forward the text message
                await app.send_message(chat_id=TO_CHANNEL_ID, text=message.text, disable_notification=True)
            print("Message forwarded successfully.")
    except Exception as e:
        print(f"Error forwarding message: {e}")


print("Bot has started.")
app.run()
