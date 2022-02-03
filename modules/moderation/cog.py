import discord 
from discord.ext import commands 


class Moderation(commands.Cog(name='Moderation',description='Moderation commands')):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is Ready\n----------------------')

    @commands.command()
    async def kick(self, member:commands.MemberConverter, *,reason:str=None):
        """Kick a member from the server"""
        if member is discord.utils.get(self.bot.get)