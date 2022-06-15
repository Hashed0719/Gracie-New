import discord

import random, datetime 

from discord import Embed
from discord.ext import commands
from discord.commands.core import slash_command

from Assets import constants

# from dislash import slash_command,Option,OptionType

from Utils.TenorGifsupport import getGif
from Utils.SomeFunctions import get_list

class slashcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
  # gracie = discord.SlashCommandGroup("gracie", "commands fetched from gracie assets", guild_ids = [constants.guild_id])
    guild_id = [constants.guild_id]
  
  # @slash_command(description="checks if slash command cog is working fine")
  # async def checkslash(self, ctx, person):
  #   await ctx.send("working fine :thumbsup:")
  
  # @slash_command(
  #   name="slap",
  #   description="slaps the user",
  #   options=[
  #       Option(
  #         "user", 
  #         "Enter the user", 
  #         OptionType.USER,
  #         required=True 
  #       )
  #   ]
  # )
  # async def slapemhard(self, ctx, user):
  #   gif_link = getGif(f"anime slap")
  #   if ctx.author.id == user.id:
  #     await ctx.send("You can't slap yourself... well technically you can... but you just can't!", ephemeral=True)
  #     raise Exception()
  #   embed = Embed(title=f"{ctx.author} slapped {user}")
  #   embed.set_image(url=gif_link)
  #   await ctx.send(embed=embed)

  # @slash_command(
  #   name="kick",
  #   description="kicks the user",
  #   options=[
  #       Option(
  #         "user", 
  #         "Enter the user", 
  #         OptionType.USER,
  #         required=True 
  #       )
  #   ]
  # )
  # async def kickemhard(self, ctx, user):
  #   gif_link = getGif(f"anime kick")
  #   if ctx.author.id == user.id:
  #     await ctx.send("You can't kick yourself!", ephemeral=True)
  #     raise Exception()
  #   embed = Embed(title=f"{ctx.author} kicked {user}")
  #   embed.set_image(url=gif_link)
  #   await ctx.send(embed=embed)

  # @slash_command(
  #   name="hug",
  #   description="slaps the user",
  #   options=[
  #       Option(
  #         "user", 
  #         "Enter the user", 
  #         OptionType.USER,
  #         required=True 
  #       )
  #   ]
  # )
  # async def hugemhard(self, ctx, user):
  #   gif_link = getGif(f"anime hug")
  #   if ctx.author.id == user.id:
  #     await ctx.send("You can't hug yourself!", ephemeral=True)
  #     raise Exception()
  #   embed = Embed(title=f"{ctx.author} hugged {user}")
  #   embed.set_image(url=gif_link)
  #   await ctx.send(embed=embed)

    @slash_command()
    async def lyric(self, ctx):
        gracie_lyrics = get_list("Gracie_Lyrics")
        await ctx.respond(random.choice(gracie_lyrics))

    @slash_command()
    async def startchain(self, ctx):
        gracie_chain = get_list("Gracie_Chain")
        await ctx.respond(random.choice(gracie_chain))

    @slash_command()
    async def finishthelyric(self, ctx):
        gracie_finishthelyric = get_list("Gracie_FinishTheLyric")
        await ctx.respond(random.choice(gracie_finishthelyric))
  
    @slash_command()
    async def intro(self, ctx):
        await ctx.respond('https://open.spotify.com/playlist/51TIRdARgx0ewyPr1PbuoX?si=ognPOCNBSLaWymms1Jc6SQ')

    @slash_command()
    async def instagram(self, ctx):
        await ctx.respond('https://www.instagram.com/gracieabrams')

    @slash_command()
    async def discography(self, ctx):
        await ctx.respond('https://open.spotify.com/playlist/37i9dQZF1DZ06evO2Cuzya?si=2c5234fcad9544e5')

  
    @slash_command()
    async def playlist(self, ctx):
        await ctx.respond('https://open.spotify.com/playlist/7Mven07omZONK1nS8o9oEo?si=3cba33f71db04ccc')

    @slash_command()
    async def mv(self, ctx):
        gracie_mvs = get_list("Gracie_Mvs")
        await ctx.respond(random.choice(gracie_mvs))

    @slash_command()
    async def unreleased(self, ctx):
        gracie_unreleased = get_list("Gracie_Unreleased")
        await ctx.respond(random.choice(gracie_unreleased))

    @slash_command()
    async def track(self, ctx):
        """sends a random track"""
        gracie_tracks = get_list("Gracie_Tracks")
        await ctx.respond(random.choice(gracie_tracks))

    @slash_command()
    async def project(self, ctx):
        gracie_projects = get_list("Gracie_Projects")
        await ctx.respond(random.choice(gracie_projects))

    @slash_command()
    async def fact(self, ctx):
        gracie_fact = get_list("Gracie_Fact")
        embed = discord.Embed(color=0x2f3136)
        embed.set_image(url=random.choice(gracie_fact))
        await ctx.respond(embed=embed)

    @slash_command()
    async def cover(self, ctx):
        gracie_covers = get_list("Gracie_Covers")
        embed = discord.Embed(color=0x2f3136)
        embed.set_image(url=random.choice(gracie_covers))
        await ctx.respond(embed=embed)

    @slash_command()
    async def taste(self, ctx):
        gracie_taste = get_list("Gracie_Taste")
        await ctx.respond(random.choice(gracie_taste))

    @slash_command()
    async def server(self, ctx):
        await ctx.respond('https://discord.gg/gracieabrams')

    @slash_command()
    async def wiki(self, ctx):
        await ctx.respond('https://gracieabrams.fandom.com/wiki/')

    @slash_command()
    async def reddit(self, ctx):
        await ctx.respond('https://www.reddit.com/r/gracie/')

  # @slash_command(description="sends ping latency")
  # async def ping(self, ctx):
  #   await ctx.send(f'Pong! **{round(self.bot.latency*1000)}ms**')

#   @slash_command(
#     description="sends a suggestion for the server",
#     options=[
#         Option("suggestion", "Enter your suggestion", OptionType.STRING, required=True)
#         # By default, Option is optional
#         # Pass required=True to make it a required arg
#     ]
# )
#   async def suggest(self,inter, suggestion):
#     channel = self.bot.get_channel(941856035461795872) # Change to the channel ID of where you want the suggestions to be posted
#     embed = discord.Embed(title="New Suggestion",    description=suggestion, color=0xDE7368) 
#     embed.set_author(name=f"{inter.author.name}#{inter.author.discriminator}", icon_url=inter.author.avatar.url)
#     embed.timestamp = datetime.datetime.utcnow()
#     embed.set_footer(text=f"ID: {inter.author.id}")
#     suggestMsg = await channel.send(embed=embed)
#     await suggestMsg.add_reaction("r:yes:939959643030040576")
#     await suggestMsg.add_reaction("r:no:939959644401590442")
#     await inter.reply(f"> **Your suggestion has been sent!** We sincerely appreciate your feedback! Please kindly wait for the server members to vote on your suggestion and the staff team to review it.", ephemeral=True) # Confirmation sent in ctx.channel after members had suggested

  
#   @slash_command(
#     description="make an anonymous confession",
#     options=[
#         Option("confession", "enter what you want to confess", OptionType.STRING, required=True)
#     ]
# )
#   async def confess(self, inter, confession):
#     await inter.send("your confession is posted!", ephemeral=True)
#     embed = discord.Embed(title="Anonymous Confession", description=f'"{confession}"', color=0x2f3136) 
#     embed.timestamp = datetime.datetime.utcnow()
#     embed.set_footer(text=f"If this confession is breaking the rules, please report to a staff member.")
#     chn = self.bot.get_channel(944096558142586880)
#     await chn.send(embed=embed)
#     audit = self.bot.get_channel(944094115543535726)
#     await audit.send(f"{inter.author.name} `({inter.author.id})` used the `/confess {confession}` command.")


    
def setup(bot):
    bot.add_cog(slashcommands(bot))
    print(f"loaded {slashcommands.__name__}")
    