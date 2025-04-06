from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from lang import T  # ⬅️ Ajout des traductions

api_id = int(input("🔑 API ID: "))
api_hash = input("🔐 API HASH: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(T["connect"])
    client.start()
    print("\n" + T["connected"])
    print(client.session.save())
    print("\n" + T["copy_session"])
    print(T["paste_session"])
    print(T["restart_script"])
