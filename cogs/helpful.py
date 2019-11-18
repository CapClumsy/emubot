import discord

from discord.ext import commands
from cogs.UtilsLib import Utils

class Helpful(commands.Cog, Utils):
    """Commands that give helpful information about emus, the Great Emu War, and the Emu Bot."""
    def __init__(self, bot):
        Utils.__init__(self)
        self.bot = bot

    @commands.command(
        name = "gamexplain",
        description = "Gives an explanation to how the Emu Bot game works",
        aliases = ['gx', 'gameexplain', 'gxplain'],
        brief = "How does the Emu Bot game work?",
        help = "Gives an in-depth explain of how to use the Emu Bot's game commands and how the Emu Bot game works"
)
    async def gamexplain(self, ctx):
        embed = discord.Embed(title='Game Explanation', description='''**In the emu bot game, you gain credits by participating in chat. You can spend these credits on emus and attack your friends with them.**
-You earn credits by sending messages.
-You can use those credits to buy emus
-The maximum amount of emus you can have is {} emus
-You can put emus on defense
-The maximum amount of emus on defense is {} emus
-You can also use emus to attack your friends
-The maximum amount of emus you can attack with at a time is {} emus
-The amount of emus you attack someone with that go over the amount of emus they have on defense grants you 700 credits for each emu.'''.format(self.MAXEMUS, self.MAXDEFENSE, self.MAXATTACK), color=0x00ff00)
        await ctx.send(embed = embed)
        
    @commands.command(
        name = 'guilds',
        description = 'Displays the number of guild the Emu Bot is a part of. Thanks to every one for supporting and using the Emu Bot',
        brief = 'Number of guilds the Emu Bot is in',
        aliases = ['guild', 'servers']
)
    async def guildcounter(self, ctx):
        msg = 'The Emu Bot is a part of `{}` guilds. Big thanks to each one for helping out and supporting the Emu Bot.'.format(len(self.bot.guilds))
        await ctx.send(msg)

    @commands.command(
        name = 'server',
        description = 'Gives a link to the Emu Bot Habitat, the Emu Bot testing and support server. If you have problem with the bot, want to suggest feature, or simply want to show your support, then this is the place to go.',
        brief = 'Join the Emu Bot testing and support server'
)
    async def serverlink(self, ctx):
        await ctx.send('Emu Bot Habitat the Emu Bot testing and support server link:\nhttps://discord.gg/2xEQkKs')

    @commands.command(
        name = 'website',
        description = 'Gives a link to the Emu Bot website',
        brief = 'Gives a link to the Emu Bot website',
        aliases = ['site']
)
    async def websitelink(self, ctx):
        await ctx.send('Emu Bot website link:\nhttps://sites.google.com/view/emu-bot-habitat/home')

    @commands.command(
        name = 'history',
        description = 'History of the Great Emu War',
        brief = 'History of the Great Emu War'
)
    async def historyytlink(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=QzYlI-W4sg8')

    @commands.command(
        name = 'war',
        description = 'The Wikipedia link to the page on the Great Emu War',
        brief = 'Information about the war'
)
    async def warwikilink(self, ctx):
        await ctx.send('https://en.wikipedia.org/wiki/Emu_War')

def setup(bot):
    bot.add_cog(Helpful(bot))
