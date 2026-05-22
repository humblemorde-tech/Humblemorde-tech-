async def ping(msg, args, bot):
    await msg.reply("Pong! Speed: fast")

async def owner(msg, args, bot):
    await msg.reply("Owner: https://facebook.com/slomo254")

async def alive(msg, args, bot):
    await msg.reply("Humble Morde✈️ is online ✅")

async def runtime(msg, args, bot):
    await msg.reply("Uptime: 2h 34m") # replace with real uptime calc

async def script(msg, args, bot):
    await msg.reply("Repo: https://github.com/yourname/humble-morde")

# Tag category for menu grouping
ping.category = "general"
owner.category = "general"
alive.category = "general"
runtime.category = "general"
script.category = "general"

# Export dict so Main.py can load them
commands = {
    "ping": ping,
    "owner": owner,
    "alive": alive,
    "runtime": runtime,
    "script": script,
}
