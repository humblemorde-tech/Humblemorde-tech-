async def ytmp3(msg, args, bot):
    if not args: return await msg.reply("Use:.ytmp3 <youtube url>")
    await msg.reply("Downloading audio... Add yt-dlp logic")

async def ytmp4(msg, args, bot):
    if not args: return await msg.reply("Use:.ytmp4 <youtube url>")
    await msg.reply("Downloading video... Add yt-dlp logic")

async def tiktok(msg, args, bot):
    if not args: return await msg.reply("Use:.tiktok <url>")
    await msg.reply("Downloading tiktok... Add API logic")

async def igdl(msg, args, bot):
    if not args: return await msg.reply("Use:.igdl <instagram url>")
    await msg.reply("Downloading instagram...")

async def fbdl(msg, args, bot):
    if not args: return await msg.reply("Use:.fbdl <facebook url>")
    await msg.reply("Downloading facebook...")

async def gitclone(msg, args, bot):
    if not args: return await msg.reply("Use:.gitclone <repo url>")
    await msg.reply("Cloning repo...")

async def apk(msg, args, bot):
    if not args: return await msg.reply("Use:.apk <app name>")
    await msg.reply("Searching apk...")

async def play(msg, args, bot):
    if not args: return await msg.reply("Use:.play <song name>")
    await msg.reply(f"Searching: {' '.join(args)}")

for cmd in [ytmp3, ytmp4, tiktok, igdl, fbdl, gitclone, apk, play]:
    cmd.category = "downloader"

commands = {
    "ytmp3": ytmp3, "ytmp4": ytmp4, "tiktok": tiktok, "igdl": igdl,
    "fbdl": fbdl, "gitclone": gitclone, "apk": apk, "play": play
}
