import os, sys

async def restart(msg, args, bot):
    if msg.sender.split('@')[0]!= os.getenv("OWNER_NUMBER"): return
    await msg.reply("Restarting...")
    os.execv(sys.executable, ['python'] + sys.argv)

async def broadcast(msg, args, bot):
    if msg.sender.split('@')[0]!= os.getenv("OWNER_NUMBER"): return
    if not args: return await msg.reply("Use:.broadcast <text>")
    chats = await bot.get_chats()
    for chat in chats: await bot.send_message(chat.id, " ".join(args))
    await msg.reply(f"Broadcast sent to {len(chats)} chats")

async def block(msg, args, bot):
    if msg.sender.split('@')[0]!= os.getenv("OWNER_NUMBER"): return
    if msg.quoted: await bot.block_user(msg.quoted.sender)
    await msg.reply("Blocked")

async def unblock(msg, args, bot):
    if msg.sender.split('@')[0]!= os.getenv("OWNER_NUMBER"): return
    if msg.quoted: await bot.unblock_user(msg.quoted.sender)
    await msg.reply("Unblocked")

for cmd in [restart, broadcast, block, unblock]:
    cmd.category = "owner"

commands = {
    "restart": restart, "broadcast": broadcast, "block": block, "unblock": unblock
}
