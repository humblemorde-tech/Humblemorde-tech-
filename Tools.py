import requests, qrcode, io

async def qr(msg, args, bot):
    if not args: return await msg.reply("Use:.qr <text>")
    img = qrcode.make(" ".join(args))
    bio = io.BytesIO()
    img.save(bio, "PNG")
    await msg.reply_image(bio.getvalue(), "QR Code")

async def weather(msg, args, bot):
    if not args: return await msg.reply("Use:.weather <city>")
    await msg.reply(f"Weather for {' '.join(args)}: 25°C ☀️") # Add real API

async def translate(msg, args, bot):
    if len(args) < 2: return await msg.reply("Use:.translate en Hello")
    await msg.reply(f"Translated: {' '.join(args[1:])}") # Add googletrans

async def calc(msg, args, bot):
    if not args: return await msg.reply("Use:.calc 5+5")
    try: await msg.reply(f"Result: {eval(''.join(args))}")
    except: await msg.reply("Invalid")

async def ssweb(msg, args, bot):
    if not args: return await msg.reply("Use:.ssweb <url>")
    await msg.reply("Taking screenshot...") # Add screenshot API

async def sticker(msg, args, bot):
    if not msg.quoted_image: return await msg.reply("Reply to image")
    await msg.reply_sticker(msg.quoted_image) # Add conversion

async def toimg(msg, args, bot):
    if not msg.quoted_sticker: return await msg.reply("Reply to sticker")
    await msg.reply_image(msg.quoted_sticker) # Add conversion

async def lyrics(msg, args, bot):
    if not args: return await msg.reply("Use:.lyrics <song>")
    await msg.reply(f"Lyrics for {' '.join(args)}...") # Add lyrics API

for cmd in [qr, weather, translate, calc, ssweb, sticker, toimg, lyrics]:
    cmd.category = "tools"

commands = {
    "qr": qr, "weather": weather, "translate": translate, "calc": calc,
    "ssweb": ssweb, "sticker": sticker, "toimg": toimg, "lyrics": lyrics
}
