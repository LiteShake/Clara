
#region IMPORTS

import discord
from discord.ext import commands, tasks

#endregion

#region CLARA CLASS

class ClaraBot(commands.Bot) :
    
    def __init__(self, token:str ):
        
        self.TOKEN:str = token
        super().__init__(
            command_prefix  = "c>",
            intents         = discord.Intents.all()
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
        
        return await super().on_message(message)
            

#endregion
