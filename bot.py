#imports stuff
import discord
import json
import os.path
import threading
import random
import asyncio

from cogs.masterclass import masterclass
from discord.ext import commands

#gives token -----------------------------------------------------------------
with open('TOKEN.txt', 'r') as f:
    TOKEN = f.readline()


class EmuBot(commands.bot, masterclass):
    def __init__(self):
        DESCRIPTION = '''A discord bot to honor our best friends, the emus. 
        With this bot you can use fun (and pointless) commands, earn credits by chatting, use those credits to buy emus, and use those emus to attack or defend against your friends.'''
        
        commands.bot.__init__(command_prefix = 'e!'
                             description = DESCRIPTION
                             case_insensitive = True)
        masterclass.__init__()
        
        self.COGS = ['cogs.fun', 'cogs.game', 'cogs.misc']
        for cog in self.COGS:
            self.load_extension(cog)
            
    async def on_message(self, message):
        #spam protection to give credits or start timer -------------------------------
        if (not message.author.id in self.SPAMCATCH) or (message.author.id in self.SPAMCATCH and not self.SPAMCATCH[message.author.id]):
            add_stats(message.author.id, 10, 'credits')
            self.SPAMCATCH[message.author.id] = True
            def spamtimer():
                self.spamswitch(message.author.id)
            t = threading.Timer(10.0, spamtimer)
            t.start()
            
        await self.process_commands(message)
    
    async def on_command_error(ctx, error):
        await ctx.send(str(error))
        print(error)
    
    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        await self.change_presence(game=discord.Game(name= "Say e!help"))
        

#runs the bot -------------------------------------------------------------
if __name__ == '__main__':
    b = EmuBot()
    b.run(TOKEN)
