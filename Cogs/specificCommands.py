import disnake 

import datetime

from disnake.commands import core 
from disnake.ext import commands
from disnake import InputTextStyle, ui

from Assets import constants



class confess_modal(ui.Modal):
    def __init__(self, bot: disnake.Bot):
        super().__init__(title="Confess")
        self.bot = bot

        self.add_item(
            ui.InputText(
            style=InputTextStyle.short,
            label="Name",
            required=False,
            placeholder='Leave Empty if "Anonymous" confession',
            )
        )
        
        self.add_item(
            ui.InputText(
            style=InputTextStyle.long,
            label="Your Confession",
            placeholder="Your confession may be completely anonymous but you could still be banned for breaking server laws."
            )
        )

    async def callback(self, interaction :disnake.Interaction):
        author = interaction.user
        with open("Assets/Bans/confessban.txt") as file:
            list = file.readlines()
            ban_list = [int(x.rstrip("\n")) for x in list]
        if author.id in ban_list:
            msg = "Looks like you are banned from using this command!"
            await interaction.response.send_message(msg, delete_after=5)
            self.stop()
            return
            
        await interaction.response.send_message("Thanks for your confession!", ephemeral=True)

        if not self.children[0].value:
            name = ""
            embed_title = "Anonymous Confession" 
        else:
            name = self.children[0].value.strip()
            embed_title = f"{name}'s Confession" 
        confession_description = self.children[1].value

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
    
        self.stop()    


class special_commands(commands.Cog):
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
                
        modal = confess_modal(self.bot)
        view = MyView(modal=modal)
        sent_button = await ctx.send(".", view=view)
        await modal.wait()
        await sent_button.delete()

    @core.slash_command(name="confess")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def confess_slash(self, ctx :disnake.ApplicationContext):
        """Confess to your heart's content '-'"""
        modal = confess_modal(self.bot)
        await ctx.send_modal(modal)
    
    @confess.error
    async def local_handler(self, ctx, error):
        await ctx.send(str(error))  

    @confess_slash.error
    async def local_handler(self, ctx, error):
        await ctx.respond(str(error))  



def setup(bot):
    bot.add_cog(special_commands(bot))
    print(f"loaded {special_commands.__name__}")


