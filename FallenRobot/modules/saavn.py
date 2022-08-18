import os
from pyrogram import filters
import wget
import requests
from FallenRobot import pbot as Mbot
from asgiref.sync import sync_to_async
from requests import get
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])
@sync_to_async
def thumb_down(album_id,img):
    with open(f"/tmp/thumbnails/{album_id}.jpg","wb") as file:
        file.write(get(img).content)
    return f"/tmp/thumbnails/{album_id}.jpg"

@Mbot.on_message(filters.command('saavn') & filters.text)
async def song(client, message):
    message.chat.id
    message.from_user["id"]
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/saavn 𝙧𝙚𝙦𝙪𝙞𝙧𝙚𝙨 𝙖𝙣 𝙖𝙧𝙜𝙪𝙢𝙚𝙣𝙩.")
    if args.startswith(" "):
        await message.reply("/saavn requires an argument.")
        return ""
    pak = await message.reply('𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 😁..')
    try:
#Ahh The Shit is too long 😒
        r = requests.get(f"https://jostapi.herokuapp.com/saavn?query={args}")
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r.json()[0]["song"]
    slink = r.json()[0]["media_url"]
    ssingers = r.json()[0]["primary_artists"]
    album_id = r.json()[0]["albumid"]
    img = r.json()[0]["image"]
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await pak.edit('𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 🙂🔥..')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=f"{sname} - from saavn",thumb=thumbnail)
    os.remove(ffile)
    await pak.delete()
