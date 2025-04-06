import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from lang import T 

# === CONFIGURATION ===
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")
download_folder = 'downloads'

mode = os.environ.get("MODE", "dev").lower()

client = TelegramClient(StringSession(session_string), api_id, api_hash)
os.makedirs(download_folder, exist_ok=True)

async def choisir_channel_dev():
    print(T["connect"])
    await client.start()

    channels = []
    print("\n" + T["select_channel"] + "\n")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            channels.append(dialog)

    for i, ch in enumerate(channels):
        print(f"[{i}] {ch.name} (ID: {ch.entity.id})")

    choix = int(input("\n" + T["choose_channel"] + " "))
    canal = channels[choix]
    print(f"\n✅ {T['channel_selected']} : {canal.name} (ID: {canal.entity.id})\n")
    return canal.entity

async def get_channel_prod():
    await client.start()
    source_channel_id = int(os.environ.get("SOURCE_CHANNEL_ID"))

    async for dialog in client.iter_dialogs():
        if dialog.is_channel and dialog.entity.id == source_channel_id:
            print(f"✅ {T['source_found']} : {dialog.name} (ID: {dialog.entity.id})")

    raise ValueError(f"❌ {T['source_not_found']} {source_channel_id}")


async def main():
    await client.start()

    if mode == "prod":
        print(T["mode_prod"])
        source_chat = await get_channel_prod()
        target_channel_id = int(os.environ.get("TARGET_CHANNEL_ID"))
    else:
        print(T["mode_dev"])
        source_chat = await choisir_channel_dev()
        target_channel_id = int(os.environ.get("TARGET_CHANNEL_ID"))

    @client.on(events.NewMessage(chats=source_chat))
    async def handler(event):
        print(T["new_message"])

        await client.forward_messages(target_channel_id, event.message)
        print(f"{T['forwarded']} {target_channel_id}")

        if event.message.file:
            filename = event.message.file.name or f"file_{event.message.id}"
            print(f"{T['downloading']} : {filename}")
            path = os.path.join(download_folder, filename)
            await event.message.download_media(file=path)
            print(f"{T['saved']} : {path}")

    print(T["listening"])
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
