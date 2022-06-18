import disnake

import random, datetime 

from disnake import Embed
from disnake.ext import commands
from disnake.ext.commands import slash_command

from Assets import constants
from Assets.constants import social_links
# from dislash import slash_command,Option,OptionType

from Utils.TenorGifsupport import getGif
from Utils.SomeFunctions import get_list

import logging as log


class MySlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
  # gracie = disnake.SlashCommandGroup("gracie", "commands fetched from gracie assets", guild_ids = [constants.guild_id])
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
    async def lyric(self, inter):
        """Sends random lyrics from gracie's songs."""
        gracie_lyrics = get_list("Gracie_Lyrics")
        await inter.response.send_message(random.choice(gracie_lyrics))

    @slash_command()
    async def startchain(self, inter):
        """Starts a new lyric chain!"""
        gracie_chain = get_list("Gracie_Chain")
        await inter.response.send_message(random.choice(gracie_chain))

    @slash_command()
    async def finishthelyric(self, inter):
        """A fun game of finishing a lyric by gracie! """
        gracie_finishthelyric = get_list("Gracie_FinishTheLyric")
        await inter.response.send_message(random.choice(gracie_finishthelyric))
  
    @slash_command()
    async def intro(self, inter):
        """Sends intro playlist."""
        await inter.response.send_message('https://open.spotify.com/playlist/51TIRdARgx0ewyPr1PbuoX?si=ognPOCNBSLaWymms1Jc6SQ')

    @slash_command()
    async def instagram(self, inter):
        """Sends link to gracie's Instagram handle."""
        await inter.response.send_message('https://www.instagram.com/gracieabrams')

    @slash_command()
    async def discography(self, inter):
        """Sends gracie's discography."""
        await inter.response.send_message('https://open.spotify.com/playlist/37i9dQZF1DZ06evO2Cuzya?si=2c5234fcad9544e5')

  
    @slash_command()
    async def playlist(self, inter):
        """Sends Gracie's songs playlist."""
        await inter.response.send_message('https://open.spotify.com/playlist/7Mven07omZONK1nS8o9oEo?si=3cba33f71db04ccc')

    @slash_command()
    async def mv(self, inter):
        """Gets a random music video link."""
        gracie_mvs = get_list("Gracie_Mvs")
        await inter.response.send_message(random.choice(gracie_mvs))

    @slash_command()
    async def unreleased(self, inter):
        """Sends a link to one of gracie's unreleased songs."""
        gracie_unreleased = get_list("Gracie_Unreleased")
        await inter.response.send_message(random.choice(gracie_unreleased))

    @slash_command()
    async def track(self, inter):
        """sends a random track"""
        gracie_tracks = get_list("Gracie_Tracks")
        await inter.response.send_message(random.choice(gracie_tracks))

    @slash_command()
    async def project(self, inter):
        """Sends a random gracie project."""
        gracie_projects = get_list("Gracie_Projects")
        await inter.response.send_message(random.choice(gracie_projects))

    @slash_command()
    async def fact(self, inter):
        """Tells a fact about gracie."""
        gracie_fact = get_list("Gracie_Fact")
        embed = disnake.Embed(color=0x2f3136)
        embed.set_image(url=random.choice(gracie_fact))
        await inter.response.send_message(embed=embed)

    @slash_command()
    async def cover(self, inter):
        """Sends covers."""
        gracie_covers = get_list("Gracie_Covers")
        embed = disnake.Embed(color=0x2f3136)
        embed.set_image(url=random.choice(gracie_covers))
        await inter.response.send_message(embed=embed)

    @slash_command()
    async def taste(self, inter):
        """Sends gracie's random rating for your choice."""
        gracie_taste = get_list("Gracie_Taste")
        await inter.response.send_message(random.choice(gracie_taste))

    @slash_command()
    async def server(self, inter):
        """Sends 'Gracie Abrams' server link."""
        await inter.response.send_message('https://discord.gg/gracieabrams')

    @slash_command()
    async def social(self, inter):
        """Sends gracie's social handles."""
        embed = Embed()
        embed.title = "Gracie's Social handles"
        embed.color = disnake.Colour.dark_teal()
        embed.set_thumbnail(url=random.choice(get_list("Gracie_Images")))
        for media, link in social_links.items():
            for index in range(-1,-len(link),-1):
                if link[index] == "/":
                    name = link[index+1:]
                    break
            embed.add_field(name=f"{media}", value=f"[{name}]({link})", inline=True)
        await inter.response.send_message(embed=embed)
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
#     embed = disnake.Embed(title="New Suggestion",    description=suggestion, color=0xDE7368) 
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
#     embed = disnake.Embed(title="Anonymous Confession", description=f'"{confession}"', color=0x2f3136) 
#     embed.timestamp = datetime.datetime.utcnow()
#     embed.set_footer(text=f"If this confession is breaking the rules, please report to a staff member.")
#     chn = self.bot.get_channel(944096558142586880)
#     await chn.send(embed=embed)
#     audit = self.bot.get_channel(944094115543535726)
#     await audit.send(f"{inter.author.name} `({inter.author.id})` used the `/confess {confession}` command.")


    
def setup(bot):
    bot.add_cog(MySlashCommands(bot))
    log.info(f"loaded {MySlashCommands.__name__}")
    