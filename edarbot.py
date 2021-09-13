# Multipurpose DnD Session Aid bot for personal use
# William Lee

import discord
from discord.ext import commands
import logging
import random
import asyncio
import youtube_dl

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

# Logging support
# TODO: personalize logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''Personal multipurpose DnD Session Aid bot.\nIn memoriam of the fallen Robo Edar.'''
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as \"{bot.user.name}\", ID {bot.user.id}")
    print("Have a nice session!")
    print('===---===')


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except (ValueError, Exception):
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


bot.run('ODg3MDc4MzQ0MjkyNjk2MDkw.YT-6Fg.2CWVdREOjMYRxV1VcrfX7lJZj9E')
