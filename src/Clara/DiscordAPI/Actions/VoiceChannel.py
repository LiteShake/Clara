
#region IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import discord
#endregion

#region VC Methods

async def JoinVoiceChannel(message: discord.Message) -> discord.VoiceClient:
    
    # 1. Type hint should be discord.VoiceChannel (PascalCase)
    # 2. message.author.voice.channel is a normal property, do NOT use 'await'
    channel: discord.VoiceChannel = message.author.voice.channel
    
    # 3. channel.connect() returns a discord.VoiceClient object
    connection: discord.VoiceClient = await channel.connect(
        self_deaf = False,
        timeout   = 60.0
    )
    
    return connection

async def LeaveVoiceChannel( message: discord.Message, channel : discord.VoiceClient ) -> None:
    
    if( channel ) :
        await channel.disconnect()

#endregion
