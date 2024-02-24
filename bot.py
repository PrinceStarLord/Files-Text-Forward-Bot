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

# @app.on_message(filters.chat(FROM_CHANNEL))
# async def forward_files(client, message):
#     if not message.chat.type == "private":
#         try:
#             print("Received message from channel:", message.chat.id)
#             if message.media:
#                 print("Media message received:", message.media)
                
#                 if message.media.document or message.media.video:
#                     file_name = message.media.document.file_name if message.media.document else message.media.video.file_name
#                     print("File name:", file_name)
                    
#                     cleaned_name = re.sub(r'[-_+=?:;\'"{\}\[\]\\\/()]+', ' ', file_name)
#                     cleaned_name = re.sub(r'\.\w+', '', cleaned_name)

#                     if cleaned_name not in forwarded_files:
#                         forwarded_files.add(cleaned_name)
#                         caption = f"<b>{cleaned_name}</b>\n\nBy @FSearch2bot"
#                         await app.send_message(TO_CHANNEL_ID, caption, parse_mode='html')
#                         print("Forwarded media message")
#                 elif message.media.text:
#                     print("Text message received:", message.media.text)
#                     await app.send_message(TO_CHANNEL_ID, message.media.text, link_preview=False, parse_mode='html')
#                     print("Forwarded text message")
#             else:
#                 print("No media or text found in the message")
#         except Exception as e:
#             print(f"Error: {e}")
#             print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


@app.on_message(filters.chat(FROM_CHANNEL))
async def forward_message(client, message):
    try:
        # Forward the message to the destination channel
        await app.forward_messages(chat_id=TO_CHANNEL_ID, from_chat_id=message.chat.id, message_ids=message.message_id)
        print("Message forwarded successfully.")
    except Exception as e:
        print(f"Error forwarding message: {e}")

print("Bot has started.")
app.run()
