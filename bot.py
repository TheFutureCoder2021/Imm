import discord , logging 
from discord.ext import commands 
from config import *


bot =  commands.Bot(command_prefix=BOT_PREFIX, intents=BOT_INTENTS)

bot.urls = BOT_API_URLS

bot.banned_words = BOT_BANNED_WORDS


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}\n{bot.user.id}\n----------------------')



@bot.event
async def on_message(message:discord.Message):
    if any(words in message.context for words in bot.banned_words):
        await message.delete()
        await message.channel.send(f'{message.author.mention} your message has been deleted for containing banned words.')


@bot.command()
async def ping(ctx:commands.Context):
    """Pong!"""
    await ctx.reply(f'Pong! **{round(bot.latency * 1000)}**`ms`')


def main():
    bot.run(BOT_TOKEN)
    logging.basicConfig(level=logging.INFO)
    load_cogs(bot, 'modules', 'cog.py')


if __name__ in "__main__":
    main()