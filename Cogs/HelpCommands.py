import disnake
from disnake.ext import commands

class MyPaginator():
    def __init__(self, embeds: list[disnake.Embed]) -> None:
        self.embeds = embeds 
        
class CustomHelpCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__(command_attrs = {"help":"Shows this command"})
        self.bot = bot 

    async def send_bot_help(self, mapping: dict):
        bot_commands = self.bot.commands
        paginator = commands.Paginator(max_size=10)
        [paginator.add_line(f"{x}") for x in range(12)]

def setup(bot):
    bot.add_cog()