import random, datetime

from disnake import Embed, Colour
from disnake.ext import commands

from Utils.SomeFunctions import get_list

from Assets.constants import channel_id
from Assets.constants import (
playlist,
intro_playlist,
discography_playlist,
server_link,
social_links
)


class graciecommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command()
    async def ping(self, ctx):
        """Sends the bot's latency."""
        await ctx.reply(f'Pong! **{round(self.bot.latency*1000)}ms**')

    @commands.command(name = "server")
    async def server(self, ctx):
        """Sends 'Gracie Abrams' server link."""
        await ctx.send(server_link)

    @commands.command(name = "taste")
    async def taste(self, ctx):
        """Sends gracie's random rating for your choice."""
        await ctx.reply(random.choice(get_list("Gracie_Taste")))
  
    @commands.command(aliases=["album","ep"])
    async def project(self, ctx):
        """Sends a random gracie project."""
        await ctx.send(random.choice(get_list("Gracie_Projects")))

    @commands.command(name = "unreleased")
    async def unreleased(self, ctx):
        """Sends a link to one of gracie's unreleased songs."""
        await ctx.send(random.choice(get_list("Gracie_Unreleased")))
  
    @commands.command(name="mv")
    async def mv(self, ctx):
        """Gets a random music video link."""
        await ctx.send(random.choice(get_list("Gracie_Mvs")))
  
    @commands.command(name = "playlist")
    async def playlist(self, ctx):
        """Sends Gracie's songs playlist."""
        await ctx.send(playlist)

    @commands.command(name = "discography")
    async def discography(self, ctx):
        """Sends gracie's discography."""
        await ctx.send(discography_playlist)   

    @commands.command(name = "intro")
    async def intro(self, ctx):
        """Sends intro playlist."""
        await ctx.send(intro_playlist)

    @commands.command(name = "cover")
    async def cover(self, ctx):
        """Sends covers."""
        embed = Embed(color=0x2f3136)
        embed.set_image(url=random.choice(get_list("Gracie_Covers")))
        await ctx.send(embed=embed)

    @commands.command(name = "lyric", alias = ["lyrics",])
    async def lyric(self, ctx):
        """Sends random lyrics from gracie's songs."""
        gracie_lyrics = get_list("Gracie_Lyrics")
        await ctx.send(random.choice(gracie_lyrics))

    @commands.command(aliases=["funfact"])
    async def fact(self, ctx):
        """Tells a fact about gracie."""
        embed = Embed(color=0x2f3136)
        embed.set_image(url=random.choice(get_list("Gracie_Fact")))
        await ctx.send(embed=embed)

    @commands.command(name = "track")
    async def track(self, ctx):
        """Sends a random track."""
        gracie_tracks = get_list("Gracie_Tracks")
        await ctx.send(random.choice(gracie_tracks))

    @commands.command(name = "startchain")
    async def startchain(self, ctx):
        """Starts a new lyric chain!"""
        gracie_chain = get_list("Gracie_Chain")
        await ctx.send(random.choice(gracie_chain))

    @commands.command(
        name = "finishthelyric",
        alias = ["finishthelyrics",]
        )
    async def finishthelyric(self, ctx):
        """A fun game of finishing a lyric by gracie! """
        listt = get_list("Gracie_FinishTheLyric")
        await ctx.send(random.choice(listt))

    @commands.command(
        name = "social", 
        aliases = list(social_links.keys())
        )
    async def social(self, ctx):
        """Sends gracie's social handles."""
        embed = Embed()
        embed.title = "Gracie's Social handles"
        embed.color = Colour.dark_teal()
        embed.set_thumbnail(url=random.choice(get_list("Gracie_Images")))
        for media, link in social_links.items():
            for index in range(-1,-len(link),-1):
                if link[index] == "/":
                    name = link[index+1:]
                    break
            embed.add_field(name=f"{media}", value=f"[{name}]({link})", inline=True)
        await ctx.send(embed=embed)
  
  # @commands.command()
  # async def say(self, ctx, *, rep):
  #   prohibited = ["@here", "@everyone", "discord.gg/"]
  #   check = lambda a: True if a in rep else False
  #   conditions = [check(word) for word in prohibited]
  #   if any(conditions):
  #     await ctx.send("cannot say that")
  #   else:
  #     await ctx.message.delete()
  #     await ctx.send(rep)
  #     audit = self.bot.get_channel(channel_id.audit)
  #     await audit.send(f"{ctx.author.name} `({ctx.author.id})` used the '/say {rep}' command")

    @commands.command()
    async def suggest(self, ctx,*,suggestion):
        """Send suggestions for the server from this command!"""
        channel = self.bot.get_channel(941856035461795872) # Change to the channel ID of where you want the suggestions to be posted
        embed = Embed(title="New Suggestion", description=suggestion, color=0xDE7368) 
        embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"ID: {ctx.author.id}")
        suggestMsg = await channel.send(embed=embed)
        await suggestMsg.add_reaction("r:yes:939959643030040576")
        await suggestMsg.add_reaction("r:no:939959644401590442")
        await ctx.message.add_reaction("☑️")
        await ctx.send(f"> **{ctx.author.mention}, your suggestion has been sent!** We sincerely appreciate your feedback! Please kindly wait for the server members to vote on your suggestion and the staff team to review it.") # Confirmation sent in ctx.channel after members had suggested

    @suggest.error
    async def suggest_error(ctx, error):
        await ctx.send(f"⚠️ **{error}**")  

# @bot.command()
# async def addimg(ctx,link):
#   ('gracieims.txt').append(link)
#   if link in ('gracieimgs.txt'):
#     await ctx.reply("**Your image has been added, thanks for submitting!**")

# @bot.command()
# async def removeimg(ctx,link):
#   ('gracieims.txt').remove(link)
#   if link in ('gracieimgs.txt'):
#     await ctx.reply("**Your image has been removed from the database.**")

# @inter_client.slash_command(description="sends a random image of gracie")
# async def img(ctx):
#  with open('gracieimgs.txt' ,mode='r') as f:
#     contents = f.readlines() 
#     embed = discord.Embed(color=0x2f3136)
#     embed.set_image(url=random.choice(contents))
#     await ctx.send(embed=embed)
# @bot.command(aliases=["pic","image","pfp","picture"])
# async def img(ctx):
#  with open('gracieimgs.txt' ,mode='r') as f:
#     contents = f.readlines() 
#     embed = discord.Embed(color=0x2f3136)
#     embed.set_image(url=random.choice(contents))
#     await ctx.send(embed=embed)

# @inter_client.slash_command(description="sends a random gif of gracie")
# async def gif(ctx):
#  embed = discord.Embed(color=0x2f3136)
#  embed.set_image(url=random.choice(gracie_gifs))
#  await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(graciecommands(bot))
    print(f"loaded {graciecommands.__name__}")