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
    'joke-api': 'https://sv443.net/jokeapi/v2/joke/Any?type=single&blacklistFlags=nsfw,religious,political,racist,sexist'
}

def banned_words():
    with open('banned_words.json') as f:
        banned_words = json.load(f)
    return banned_words['swear_words']

BOT_BANNED_WORDS = banned_words()
