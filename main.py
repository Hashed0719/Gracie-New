import disnake
from disnake.ext import commands
from disnake import __version__
print(__version__)

from keep_alive import keep_alive

from dotenv import load_dotenv

from Assets import constants

import os

import logging as log

log.basicConfig(
    filemode="w",
    filename="bot.log",
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    level=log.INFO
)

BOT_PREFIX = ";"

def _get_prefix(bot: commands.Bot, message: disnake.Message):
    first_content = message.content.split()[0]
    commands_invoked = [
        command for command in bot.commands 
        if command.name.lower() in first_content.lower()
        or any(alias in first_content.lower() for alias in command.aliases)
    ]
    for command in commands_invoked:
        if hasattr(command.cog, "prefix"):
            if command.cog.prefix + command.name.lower() == first_content.lower():
                return command.cog.prefix 
        else:
            return BOT_PREFIX

bot = commands.Bot(
    command_prefix=_get_prefix,
    activity=disnake.Activity(
        type=disnake.ActivityType.watching,
        name="you half-drunk happy"
    ),
    intents=disnake.Intents.all(),
    debug_guilds = [constants.guild_id]
)
    
@bot.event
async def on_ready():
    print(f"Succesfully connected as {bot.user}")

@bot.event
async def on_message(msg: disnake.Message):
    if f"<@{bot.user.id}>" in msg.content:
        await msg.reply(f"Hello there! My prefix is `{BOT_PREFIX}`")
    else:
        await bot.process_commands(msg)

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