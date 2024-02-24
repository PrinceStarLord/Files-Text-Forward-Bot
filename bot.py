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

async def send_with_delay(chat_id, text):
    await asyncio.sleep(1)  # Adjust the delay time as needed
    await app.send_message(chat_id=chat_id, text=text, disable_notification=True)

@app.on_message(filters.chat(FROM_CHANNEL))
async def forward_message(client, message):
    try:
        # Check if the message is not from a private chat and not a poll
        if not message.chat.type == "private" and not message.poll:
            # Check if the message contains media
            if message.document or message.video:
                media = message.document or message.video
                file_name = re.sub(r'[^\w\s.-]', '', media.file_name)  # Remove special characters
                file_name = file_name.replace('_', ' ')  # Replace underscores with blank space
                file_name = re.sub(r'\.(mkv|mp4)', '', file_name)  # Remove .mkv and .mp4 extensions
                caption = f"**{file_name} Uploaded By : @FSearch2Bot**"
                await send_with_delay(TO_CHANNEL_ID, caption)
                print("Message forwarded successfully.")
    except Exception as e:
        print(f"Error forwarding message: {e}")


print("Bot has started.")
app.run()
