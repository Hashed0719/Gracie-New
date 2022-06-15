import discord
from discord.ext import commands
from discord import __version__

from keep_alive import keep_alive

from dotenv import load_dotenv

from Assets import constants

import os

import logging 


print(__version__)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(";"),
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="you half-drunk happy"
    ),
    intents=discord.Intents.all(),
    debug_guilds = [constants.guild_id]
)
    
@bot.event
async def on_ready():
    print(f"Succesfully connected as {bot.user}")

extensions = [
    "Cogs._initManager",
    "Cogs.eventListeners",
    "Cogs.helpCommand",
    "Cogs.imagesAndGifs",
    "Cogs.slashCommands",
    "Cogs.gracieCommands",
    "Cogs.specificCommands"
]

[bot.load_extension(ext) for ext in extensions]

keep_alive()
load_dotenv()
bot.run(os.environ["token"])