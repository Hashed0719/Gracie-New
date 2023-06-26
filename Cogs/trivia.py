import disnake 
from disnake import ModalInteraction, TextInputStyle, Embed
from disnake.ext import commands
from disnake.ext.commands import Context, Command, slash_command, command
from disnake.ui import View, Modal, Item, TextInput

from Assets import constants
from Utils import db

import logging 


class Qna_Modal(Modal):
    def __init__(self) -> None:
        super().__init__(
            title="We are collecting questions for Trivia!",
            components=[
                TextInput(
                    label="Question",
                    style=TextInputStyle.multi_line,
                    min_length=20,
                    custom_id="question"
                ), 
                TextInput(
                label="Answer",
                style=TextInputStyle.single_line,
                min_length=1,
                max_length = 20,
                custom_id="answer"
                ) 
            ]
        )

    async def callback(self, interaction: ModalInteraction, /) -> None:
        """
        Questions and there answers will be saved to Gracie.db,
        table name 'Trivia', 
        table format (Question varchar, Answer varchar, User varchar))
        """
        return await super().callback(interaction)
        
    async def callback(self, interaction: ModalInteraction) -> None:

        return await super().callback(interaction)


class MyView(disnake.ui.View):
    def __init__(self, *, timeout=180, modal):
        super().__init__(timeout=timeout)
        self.modal = modal 

    @disnake.ui.button(label="Button", style=disnake.ButtonStyle.primary) #label has unicoded blank character for sending empty 
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(self.modal)

class Admins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @command(name="getmodal")
    async def trivia(self, ctx: Context):
        await ctx.reply("⠀", view=MyView(modal=Qna_Modal(self.bot)))

    @slash_command(name="uploadquestion")
    async def send_view(
        self, 
        inter   , 
        question: str, 
        opt1: str,
        opt2: str,  
        opt3: str, 
        opt4: str,
        correct: int, 
        *args
    ):
        """Hey we are collecting questions for trivia, contribute!"""

        user_name = inter.author.name
        uploaded = db.upload_question(
            question,
            opt1,
            opt2,
            opt3, 
            opt4, 
            correct,
            user_name
        )

        if uploaded:
            await inter.response.send_message(
                "✅ Thanks! Your question is recorded.", 
                ephemeral=True 
                )
        else:
            await inter.response.send_message(
                "❌ Some error occured while uploading your question, contact admins.", 
                ephemeral=True
            )

    async def cog_check(  self, ctx: commands.Context):
        "a check for ensuring commands of this cog can only be invoked by admins."
        return await commands.has_any_role(1087713137291186236).predicate(ctx) #hard coded Role id must be replaced by 'constants.Roles.Admins' when commiting.

def setup(bot: commands.Bot):
    bot.add_cog(Admins(bot))
    logging.info(f"loaded trivia cog")
    