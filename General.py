import time, platform, psutil
from lib.functions import runtime_format

start_time = time.time()
BOT_NAME = "Bot ffoles"

async def ping(msg, args, bot):
    await msg.reply("Pong! 🏓")

async def alive(msg, args, bot):
    await msg.reply(f"{BOT_NAME} is alive ✅\nOwner: https://facebook.com/slomo254")

async def runtime(msg, args, bot):
    await msg.reply(f"Runtime: {runtime_format(time.time() - start_time)}")

async def owner(msg, args, bot):
    await msg.reply("Contact owner: https://facebook.com/slomo254")

async def script(msg, args, bot):
    await msg.reply("Repo: https://github.com/yourname/bot-ffoles")

async def info(msg, args, bot):
    await msg.reply(f"*Bot Info*\nName: {BOT_NAME}\nPlatform: {platform.system()}\nRAM: {psutil.virtual_memory().percent}%")

async def help(msg, args, bot):
    await msg.reply(f"Use {msg.prefix}menu to see all 40 commands")

async def speed(msg, args, bot):
    start = time.time()
    m = await msg.reply("Testing...")
    await m.edit(f"Speed: {round((time.time()-start)*1000)}ms")

async def creator(msg, args, bot):
    await msg.reply("Created by slomo254\nFacebook: https://facebook.com/slomo254")

async def donate(msg, args, bot):
    await msg.reply("Support the bot: Contact owner for donation info")

for cmd in [ping, alive, runtime, owner, script, info, help, speed, creator, donate]:
    cmd.category = "general"

commands = {
    "ping": ping, "alive": alive, "runtime": runtime, "owner": owner,
    "script": script, "info": info, "help": help, "speed": speed,
    "creator": creator, "donate": donate
  }
