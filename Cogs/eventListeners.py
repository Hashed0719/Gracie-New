from discord.ext import commands
from discord.ext.commands import Cog
from discord import Embed

class extra_commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  command = commands.command

  @Cog.listener("on_message")
  async def strawwberriess(self, message):
    content = message.content.lower()
    if message.author == self.bot.user:
      return
    if "berry" in content and "strawberry" not in content:
      await message.add_reaction(
        r":graciestrawberry:935526687351898232"
      )
    if "strawberry" in content:
      if "big" in content:
        await message.channel.send("https://cdn.discordapp.com/emojis/935526687351898232.webp?size=100&quality=lossless")
        return
      await message.channel.send ('<:graciestrawberry:935526687351898232>')
  
  @Cog.listener("on_message")
  async def last_fm(self, message):
    if message.content == "last.fm":
      link_last_fm = "https://www.last.fm"
      content=f"""    
      1. Create an account on the website {link_last_fm}\n2. Connect it to your spotify music account\n3. Go to bots and link your account by typing `,lf set (your last.fm username)`\nRun ,np to show what music youre listening to!'
      """
      image_url=f"{link_last_fm}/static/images/lastfm_logo_facebook.15d8133be114.png"
      
      embed = Embed(
        description=content
      )
      embed.set_thumbnail(url=image_url)
      await message.reply(embed=embed)

  @Cog.listener("on_message")
  async def dunnowhatthisis(self, message):
    if "i told you i was down bad" in message.content.lower():
        await message.reply('you hate to see me like that')

def setup(bot):
  bot.add_cog(extra_commands(bot))
  print(f"loaded {extra_commands.__name__}")