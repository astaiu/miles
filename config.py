from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH)
ispay = ['yes']
ispay2 = ['yes']
bot.start()