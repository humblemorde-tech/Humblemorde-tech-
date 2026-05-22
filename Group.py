async def tagall(msg, args, bot):
    if not msg.is_group: return await msg.reply("Group only")
    members = await msg.group_participants()
    text = " ".join([f"@{m.id.split('@')[0]}" for m in members])
    await msg.reply(text, mentions=members)

async def hidetag(msg, args, bot):
    if not msg.is_group: return await msg.reply("Group only")
    members = await msg.group_participants()
    await msg.reply(args[0] if args else "Hidden tag", mentions=members)

async def group(msg, args, bot):
    if not msg.is_group: return await msg.reply("Group only")
    if not args: return await msg.reply("Use:.group open/close")
    await msg.group_change_setting("announcement" if args[0]=="close" else "not_announcement")
    await msg.reply(f"Group {args[0]}ed")

async def linkgroup(msg, args, bot):
    if not msg.is_group: return await msg.reply("Group only")
    code = await msg.group_invite_code()
    await msg.reply(f"https://chat.whatsapp.com/{code}")

async def kick(msg, args, bot):
    if not msg.is_group: return await msg.reply("Group only")
    if msg.quoted: await msg.group_remove([msg.quoted.sender])
    await msg.reply("Done")

async def add(msg, args, bot):
    if not msg.is_group or not args: return await msg.reply("Use:.add 254xxx")
    await msg.group_add([f"{args[0]}@s.whatsapp.net"])
    await msg.reply("Added")

async def promote(msg, args, bot):
    if msg.quoted: await msg.group_promote([msg.quoted.sender])
    await msg.reply("Promoted")

async def demote(msg, args, bot):
    if msg.quoted: await msg.group_demote([msg.quoted.sender])
    await msg.reply("Demoted")

async def setname(msg, args, bot):
    if args: await msg.group_update_subject(" ".join(args))
    await msg.reply("Name updated")

async def setdesc(msg, args, bot):
    if args: await msg.group_update_description(" ".join(args))
    await msg.reply("Description updated")

for cmd in [tagall, hidetag, group, linkgroup, kick, add, promote, demote, setname, setdesc]:
    cmd.category = "group"

commands = {
    "tagall": tagall, "hidetag": hidetag, "group": group, "linkgroup": linkgroup,
    "kick": kick, "add": add, "promote": promote, "demote": demote,
    "setname": setname, "setdesc": setdesc
  }
