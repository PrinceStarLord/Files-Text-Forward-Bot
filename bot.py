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
                photo = message.photo[-1]  # Get the largest photo size
                caption = f"**{message.caption}\nUploaded By : @FSearch2Bot**"
                await app.send_photo(chat_id=TO_CHANNEL_ID, photo=photo.file_id, caption=caption, disable_notification=True)
            elif message.document or message.web_page:
                file_name = re.sub(r'[^\w\s.-]', '', message.document.file_name)  # Remove special characters
                file_name = file_name.replace('_', ' ')  # Replace underscores with blank space
                caption = f"**{message.caption}\nUploaded By : @FSearch2Bot**"
                await app.send_document(chat_id=TO_CHANNEL_ID, document=message.document.file_id, filename=file_name, caption=caption, disable_notification=True)
            else:
                text = f"**{message.text}\nUploaded By : @FSearch2Bot**"
                await app.send_message(chat_id=TO_CHANNEL_ID, text=text, disable_notification=True, parse_mode="MarkdownV2")
            print("Message forwarded successfully.")
    except Exception as e:
        print(f"Error forwarding message: {e}")


print("Bot has started.")
app.run()
