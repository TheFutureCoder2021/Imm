import discord , aiohttp
from discord.ext import commands 
import random 

class Fun(commands.Cog(name='Fun', description='maybe used for fun')):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is Ready\n----------------------')
    @commands.command()
    async def joke(self, ctx:commands.Context):
        """Get a random joke from the API"""
        url = self.bot.urls['joke-api']
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                joke = await resp.json()
        msg = await ctx.send(f"{joke['setup']}")
        await msg.reply(f"{joke['delivery']}")
    @commands.command()
    async def quote(self,ctx:commands.Context):
        url = self.bot.urls['zenquotes-api']
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                quote = await resp.json()
        await ctx.send(f"{quote[0]['q'] + ' - ' + quote[0]['a']}")

    @commands.command(name='8ball', aliases=['8b'])
    async def _8ball(self, ctx:commands.Context, *, question):
        """Ask the magic 8ball to describe you future"""
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            "Reply hazy, try again.",
            "Ask again later.", 
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "● Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send('Question: {}\nAnswer: {}'.format(question, random.choice(responses)))

    @commands.command(name='roll', aliases=['r'])
    async def _roll(self, ctx:commands.Context, *, args):
        """Roll a dice in NdN format"""
        try:
            rolls, limit = args.split('d')
        except:
            await ctx.send('Format has to be in NdN!')
            return
        try:
            rolls = int(rolls)
            limit = int(limit)
        except:
            await ctx.send('Format has to be in NdN!')
            return
        if rolls > 100 or limit > 100:
            await ctx.send('Too high!')
            return
        if rolls <= 0 or limit <= 0:
            await ctx.send('Too low!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)




def setup(bot:commands.Bot):
    bot.add_cog(Fun(bot))