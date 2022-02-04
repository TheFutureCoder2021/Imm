import discord 
from discord.ext import commands 
from discord.channel import TextChannel


class Utils(commands.Cog(name='Utils',description='Utility commands')):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is Ready\n----------------------')
    @commands.has_role(['MODERATOR','DEVELOPER','OWNER'])
    @commands.command(name='clear',description='Clear messages',aliases=['purge'])
    async def clear(self,ctx:commands.Context,limit:int= None):
        channel = discord.TextChannel or ctx.channel
        msg = await ctx.reply('Clearing messages...')
        await ctx.channel.purge(limit=limit)
        await msg.edit(content='Messages cleared!')
    