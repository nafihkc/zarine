import random
import asyncio
from pyrogram import filters, __version__ as pver
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from platform import python_version as pyver
from FallenRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://telegra.ph/file/47f1c6b57321808e9eb61.jpg",
    "https://telegra.ph/file/d2433e011fb8eff1650f8.mp4",
    "https://telegra.ph/file/4af05a90d3058915d20e6.jpg",
    "https://telegra.ph/file/a0a79755bc3336f47a30b.jpg",
    "https://telegra.ph/file/c35acfb3cd4699c7a9e2c.jpg",
]

SHREYXD = [
    [
        InlineKeyboardButton(text="ʟᴇɢᴇɴᴅ", url=f"https://t.me/pythonxgamer"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="Add me to you're group",
            url=f"https://t.me/misszarine_bot?startgroup=true",
        ),
    ],
]

lol = "https://telegra.ph/file/90552395a5e96d0e7fab9.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("💃")
    await asyncio.sleep(2)
    await accha.edit("wait ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkBAAI8xWLHARtUmG1OvRFyupIvRt8k39NkAAL1CAACYnB9KWTD8cH10NiqKQQ"
    )
    await umm.delete()
    await asyncio.sleep(2)
    await m.reply_photo(
        lol,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ ZARINE**
   ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [⋆ ͢ ̶ͥ ̶ ̶ͣ ͓ ̶ͫ𝘾𝘼𝙋𝙏𝘼𝙄𝞟»⃟🇺🇸 ℡](https://t.me/{OWNER_USERNAME})
  
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
   ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(SHREYXD),
    )
