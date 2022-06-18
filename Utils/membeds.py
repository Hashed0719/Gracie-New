import disnake
from disnake import Embed, Emoji, ButtonStyle, Interaction
from disnake.ext import commands
from disnake.ui import View, Item, Button, button, select

import wavelink

from Utils.gplayer import GPlayer

import logging as log
import time
import typing


class ControlView(View):
    def __init__(self, player :GPlayer, *items: Item, timeout = 180):
        super().__init__(*items, timeout=timeout)
        self.player = player

    @button(
        emoji="▶️",
        style=ButtonStyle.blurple
    )
    async def skip_button(self, button: Button, interaction: Interaction):
        log.info("used button")
        await self.player.pskip()
        await interaction.response.edit_message(view=None)

class MusicControlEmbeds:
    """A class containing all the functions to create embeds for music playback."""

    def play(player :GPlayer, track :wavelink.Track) -> typing.Tuple[disnake.Embed, disnake.ui.View]:
        """Returns embed, view for track start"""
        length = time.strftime("%M:%S", time.gmtime(track.length))
        embed = disnake.Embed(
            # title=f"Now Playing...",
            description=f"[{track.title}]\n| {length}",
            color=disnake.Colour.green()   
        )
        embed.set_author(name="Now Playing")

        if player.psource:
            track = player.psource
            embed.set_thumbnail(url=track.thumbnail)

        view = ControlView(player)
        
        return embed, view

    def skip(player, track) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"[{track.title}]",
            color=disnake.Color.yellow()
        )
        embed.set_author(name="Skipped Song")
        
        return embed