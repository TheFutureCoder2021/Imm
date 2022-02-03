import dotenv
import discord 
import os 
import json 

dotenv.load_dotenv()

BOT_NAME = 'Immortals'
BOT_DESCRIPTION = 'Only for Immortals SMP!'
BOT_INTENTS = discord.Intetns.all()
BOT_PREFIX = 'im '
BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_API_URLS = {
    'joke-api': 'https://sv443.net/jokeapi/v2/joke/Any?type=twopart&blacklistFlags=nsfw,religious,political,racist,sexist',
    'weather-api': 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=b6907d289e50d730ae9d40e3ae85d6a2',
    'zenquotes-api': 'https://zenquotes.io/api/random'
}

def banned_words():
    with open('banned_words.json') as f:
        banned_words = json.load(f)
    return banned_words['swear_words']

BOT_BANNED_WORDS = banned_words()



def load_cogs(bot,cog_folder, filename):
    for folder in os.listdir(cog_folder):
        if os.path.exists(os.path.join(cog_folder, folder, filename)):
            bot.load_extension(f'{cog_folder}.{folder}.{filename}')