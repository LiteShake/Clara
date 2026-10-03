
#region IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Clara.DiscordAPI.Bot import ClaraBot
    import discord
#endregion

#region VERSION

async def GetVersion( clientInst : ClaraBot ) -> discord.Embed :
    
    from discord import Embed
    
    placeholder_desc : str = """
    Nevver Gonna Give You Up!
    """

    # 2. Initialize the Embed with the title and description
    embed : Embed = Embed(
        title       = "Clara",
        description = placeholder_desc,
        color       = 0xff8952 # A standard Discord color
    )

    # 3. Set the bot's own avatar as the embed picture
    # We use display_avatar.url to ensure it fetches the default avatar if a custom one isn't set
    embed.set_thumbnail(url = clientInst.user.display_avatar.url)
    
    return embed

#endregion
