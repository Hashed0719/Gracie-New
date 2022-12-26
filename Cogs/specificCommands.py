import disnake 
from disnake.ext.commands import slash_command
from disnake.ext import commands
from disnake import TextInputStyle, ui

import datetime

import logging as log

from Assets import constants


class ConfessModal(ui.Modal):
    def __init__(self, bot: commands.Bot):
        super().__init__(
            title = "Confess",
            components = [
                ui.TextInput(
                        style=TextInputStyle.short,
                        label="Name",
                        required=False,
                        placeholder='Leave Empty if "Anonymous" confession',
                        custom_id="name"
                        ),
                ui.TextInput(
                        style=TextInputStyle.long,
                        label="Your Confession",
                        placeholder="Your confession may be completely anonymous but you could still be banned for breaking server laws.",
                        custom_id="confession"
                        )
                ]
        )
        self.bot = bot

    async def callback(self, interaction :disnake.ModalInteraction):
        author = interaction.user
        with open("Assets/Bans/confessban.txt") as file:
            list = file.readlines()
            ban_list = [int(x.rstrip("\n")) for x in list]
        if author.id in ban_list:
            msg = "Looks like you are banned from using this command!"
            await interaction.response.send_message(msg, delete_after=5)
            return
            
        await interaction.response.send_message("Thanks for your confession!", ephemeral=True)

        if not interaction.text_values["name"]:
            name = ""
            embed_title = "Anonymous Confession" 
        else:
            name = interaction.text_values["name"].strip()
            embed_title = f"{name}'s Confession" 
        confession_description = interaction.text_values["confession"]

    #sending confession in confess channel
        embed = disnake.Embed(
            title=embed_title,
            description=f'"{confession_description.strip()}"', 
            color=0x2f3136,
            timestamp=datetime.datetime.utcnow(),
            ) 
        
        embed.set_footer(text=f"If this confession is breaking the rules, please report to a staff member.")
        
        confess_id = constants.channel_id.confess
        confess = self.bot.get_channel(confess_id)
        test_channel = self.bot.get_channel(950181434017062942)
        await confess.send(embed=embed)

        #Logging for moderation, in audit channel.
        embed = disnake.Embed(
        description=f"id `{interaction.user.id}` used command `confess`",
        timestamp=datetime.datetime.utcnow()
        )
        embed.set_author(
            name=f"{interaction.user.name}{interaction.user.discriminator}",
            icon_url=interaction.user.display_avatar.url 
            )
        audit_id = constants.channel_id.audit
        audit_channel = self.bot.get_channel(audit_id)
        await audit_channel.send(embed=embed)
       


class SpecialCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command()
    async def confess(self, ctx :commands.Context):
        """Say something anonymously in <#944096558142586880>"""
        await ctx.message.delete()

        class MyView(disnake.ui.View):
            def __init__(self, *items, timeout = 180, modal):
                super().__init__()
                self.modal = modal

            @disnake.ui.button(label="confess", style=disnake.ButtonStyle.primary)
            async def button_callback(self, button, interaction):
                await interaction.response.send_modal(self.modal)
                
        modal = ConfessModal(self.bot)
        view = MyView(modal=modal)
        await ctx.send("Click the button below!", view=view)

    @commands.Cog.listener()
    async def on_modal_submit(self, inter: disnake.ModalInteraction):
        if inter.message:
            await inter.message.delete()

    @slash_command(name="confess")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def confess_slash(self, inter):
        """Confess to your heart's content '-'"""
        modal = ConfessModal(self.bot)
        await inter.response.send_modal(modal)
    
    @confess.error
    async def local_handler(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(str(error), delete_after=3)  

    @confess_slash.error
    async def local_handler(self, inter: disnake.interactions.ApplicationCommandInteraction, error):
        if isinstance(error, commands.CommandOnCooldown):
            await inter.response.send_message(str(error), ephemeral=True)  

def setup(bot):
    bot.add_cog(SpecialCommands(bot))
    log.info(f"loaded {SpecialCommands.__name__}")


