import disnake
from disnake.ext import commands

from Utils.SomeFunctions import get_list
import random


class ImagesCog(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command(name="PutImage", aliases = ["putimg","PutImg","putimages","putimage"], hidden = True)
  async def putImage(self, ctx, link):
    with open("gracieimgs.txt", "a") as file:
      file.writelines([f"{link}\n"])
    await ctx.reply("added :white_check_mark:")

  @commands.command(name='getimage', aliases=['img','pfp'], hidden = True)
  async def img(self, ctx):
    with open("Assets/Gracie/Gracie_Images.txt",'r') as file:
      gracie_images = file.readlines()
    embed = disnake.Embed(color=0x2f3136)
    embed.set_image(url=random.choice(gracie_images))
    await ctx.channel.send(embed=embed)

  @commands.command(name='gif', aliases=['gifs','getgif'])
  async def randomgif(self, ctx):
    """Sends a random gracie gif."""
    with open('Assets/Gracie/Gracie_Gifs.txt') as file:
      gracie_gifs = file.readlines()
    embed = disnake.Embed(color=0x2f3136)
    embed.set_image(url=random.choice(gracie_gifs))
    await ctx.channel.send(embed=embed)
   
  # @commands.command(name="RemoveImage", aliases=["rmimg"])
  # async def removeImage(self, ctx, link):
  #   with open ("gracieimgs.txt", "a") as file:
  #     data = file.readlines()
  #     if link in data:
        


def setup(bot):
    bot.add_cog(ImagesCog(bot))
    print(f"loaded {ImagesCog.__name__}")