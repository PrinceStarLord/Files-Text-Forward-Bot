import re
import logging
import asyncio
from pyrogram import Client, filters
from telethon.tl.functions.users import GetFullUserRequest
from config import *

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

forwarded_files = set()

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("I'm a Files/Video/Documents - Text Forward bot !!")

@app.on_message(filters.chat(FROM_CHANNEL))
async def forward_files(event): 
    if not event.is_private:
        try:
            # Check if the message contains any content (file, video, document, or text)
            if event.file or event.video or event.document or event.text:
                if event.file or event.video or event.document:
                    original_name = event.file.name if event.file else (event.video.attributes[0].file_name if event.video else event.document.attributes[0].file_name)
                    
                    # Remove symbols and replace underscores with spaces
                    cleaned_name = re.sub(r'[-_+=?:;\'"{\}\[\]\\\/()]+', ' ', original_name)
                    
                    # Remove file extensions
                    cleaned_name = re.sub(r'\.\w+', '', cleaned_name)

                    if cleaned_name not in forwarded_files:
                        forwarded_files.add(cleaned_name)
                        caption = f"<b>{cleaned_name}</b>\n\nBy @FSearch2bot"
                        await app.send_message(TO_CHANNEL_ID, caption, parse_mode='html')
                else:
                    # Forward text messages
                    await app.send_message(TO_CHANNEL_ID, event.text, link_preview=False, parse_mode='html')
        except Exception as e:
            print(f"Error: {e}")
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")

print("Bot has started.")
app.run()

