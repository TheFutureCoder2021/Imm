import asyncio
import discord 
from discord.ext import commands 


class Moderation(commands.Cog(name='Moderation',description='Moderation commands')):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is Ready\n----------------------')

    @commands.command()
    async def kick(self, ctx:commands.Context,member:commands.MemberConverter, *,reason:str=None):
        """Kick a member from the server"""
        if member is None:
            await ctx.reply(f'**{member}** is not found!\nPlease specify a member to kick')
        else:
            msg = await ctx.send(f'`{member}` has been found and is being kicked')
            await asyncio.sleep(2)
            await member.kick(reason=reason)
            await msg.edit(f'`{member}` has been kicked for reason {reason}')
            await member.send(f'You have been kicked from the server {ctx.guild.name} for reason: {reason}')



def setup(bot:commands.Bot):
    bot.add_cog(Moderation(bot))