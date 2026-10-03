
#region IMPORTS

import discord
from discord.ext import commands, tasks
from Clara.DiscordAPI.Actions import VoiceChannel
from Clara.DiscordAPI.Actions import Info

#endregion

#region CLARA CLASS

class ClaraBot(commands.Bot) :
    
    def __init__(self, token:str ):
        
        self.TOKEN : str = token
        self.voiceChannel: discord.VoiceClient | None = None
        self.PREFIX : str = "C>"
        self.INTENTS : discord.flags.Intents = discord.Intents.all()
        
        super().__init__(
            command_prefix  = self.PREFIX,
            intents         = self.INTENTS
        )
    
    async def on_ready(self) :
        
        print(f'Clara Online | Client: {super().user}')
    
    
        await self.change_presence(
            status      = discord.Status.online,
            activity    = discord.Activity(
                type    = discord.ActivityType.listening,
                name    ="Sick Beats!"
            )
        )
        
    async def on_message(self, message):
        
        if(message.content == "ping") : await message.reply("pong")
        
        if( message.content == "join" ) : 
            self.connection = await VoiceChannel.JoinVoiceChannel( message = message )
            
        if( message.content == "leave" ) :
            await VoiceChannel.LeaveVoiceChannel(
                message = message,
                channel = self.connection
            )
        
        if( message.content == "C>version" ) :
            
            await message.reply(
                embed = await Info.GetVersion( clientInst = super() )
            )
        
        return await super().on_message(message)
            

#endregion
