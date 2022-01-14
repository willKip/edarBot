# Multipurpose DnD Session Aid bot for personal use
# William Lee

# TODO: better help messages

import os
import discord
from discord.ext import commands
token = os.environ['DISCORD_TOKEN']
import logging


# Logging support
# TODO: personalize logging
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

description = """Personal multipurpose DnD Session Aid bot.\nIn memoriam of the fallen Robo Edar."""
intents = discord.Intents.default()
edarbot = commands.Bot(command_prefix="!", description=description, intents=intents)

edarbot.load_extension("cogs.general")
edarbot.load_extension("cogs.music")


@edarbot.event
async def on_ready():
    print(f"Logged in as \"{edarbot.user}\", ID {edarbot.user.id}")
    print("Have a nice session!")
    print("=" * 10 + "-" * 20 + "=" * 10)


edarbot.run(token)
