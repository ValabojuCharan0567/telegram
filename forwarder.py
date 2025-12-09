import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION_STRING")

# Channels to read from (usernames, no @)
SOURCE_CHANNELS = [
    "TechFactsDeals",
    "extrape",
    "iamprasadtech",
    "charan0678"     # your test channel
]

# Forward messages to this bot
TARGET_CHANNEL = "ExtraPeBot"

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def forward_message(event):
    try:
        await client.send_message(TARGET_CHANNEL, event.message)
        print("Forwarded:", event.message.text)
    except Exception as e:
        print("Error forwarding:", e)

print("USERBOT RUNNING AS USER SESSION…")
client.start()
print("Forwarding active…")
client.run_until_disconnected()
