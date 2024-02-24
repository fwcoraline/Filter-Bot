import nextcord
from nextcord.ext import commands
from nextcord.utils import find
import random
import json

class main_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        filtered_words = ['filtered_words.json']  
        for word in filtered_words:
            if word in msg.content:
                await msg.delete()
        await self.bot.process_commands(msg)

def setup(bot):
    bot.add_cog(main_commands(bot))