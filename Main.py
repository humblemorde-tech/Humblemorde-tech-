import os, asyncio, importlib
from flask import Flask, request, render_template_string, send_from_directory
from threading import Thread
from pybaileys import WhatsApp

app = Flask(__name__)
bot = None
commands = {}
prefix = os.getenv("PREFIX", ".")
owner = os.getenv("OWNER_NUMBER", "")
session_name = os.getenv("SESSION_NAME", "session")

# Load all commands from /commands folder
def load_commands():
    for file in os.listdir("commands"):
        if file.endswith(".py") and file!= "__init__.py":
            module = importlib.import_module(f"commands.{file[:-3]}")
            if hasattr(module, "commands"):
                commands.update(module.commands)
    print(f"Loaded {len(commands)} commands")

with open("lib/pairing.html", "r") as f:
    PAIR_HTML = f.read()

@app.route("/", methods=["GET", "POST"])
@app.route("/pair", methods=["GET", "POST"])
def pair():
    global bot
    code, error = None, None
    if request.method == "POST":
        number = request.form.get("number", "").strip().replace("+", "").replace(" ", "")
        if not number.isdigit() or len(number) < 10:
            error = "Invalid number. Use country code: 254712345678"
        else:
            try:
                if bot is None: error = "Bot starting... try in 10s"
                else:
                    code = bot.request_pairing_code(number).replace("-", "")
            except Exception as e: error = str(e)
    return render_template_string(PAIR_HTML, code=code, error=error, total_cmds=len(commands))

async def start_bot():
    global bot
    load_commands()
    bot = WhatsApp(session_name=session_name)

    @bot.on("connection_update")
    async def on_conn(update):
        if update.connection == "open": print("Bot Connected")

    @bot.on("messages")
    async def on_msg(msg):
        if not msg.text or not msg.text.startswith(prefix): return
        args = msg.text[len(prefix):].split()
        cmd = args[0].lower()
        args = args[1:]

        if cmd in commands:
            try: await commands[cmd](msg, args, bot)
            except Exception as e: await msg.reply(f"Error: {e}")
        elif cmd == "menu":
            cats = {}
            for name, func in commands.items():
                cat = getattr(func, "category", "misc")
                cats.setdefault(cat, []).append(name)
            menu = f"*Humble Morde✈️* - {len(commands)} Commands\n"
            for cat, cmds in cats.items():
                menu += f"\n*{cat.upper()}*\n" + " ".join([prefix + c for c in cmds]) + "\n"
            menu += f"\nOwner: https://facebook.com/slomo254"
            await msg.reply(menu)

    await bot.connect()

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    asyncio.run(start_bot())
