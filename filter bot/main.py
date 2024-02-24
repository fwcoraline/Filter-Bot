import nextcord
from nextcord.ext import commands
from nextcord.utils import find
from datetime import datetime
import json

bot = commands.Bot(command_prefix='.', intents=nextcord.Intents.all())
TOKEN = ""

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
@commands.has_permissions(administrator=True)
async def enable_filter(ctx):
    await bot.load_extension('cog.main_commands')

@bot.event
async def on_message(msg):
    for word in 'filtered_words.json':
        if word in msg.content:
            await msg.delete()
            
    await bot.process_commands(msg)

bot.load_extension('main_commands')
bot.run(TOKEN)