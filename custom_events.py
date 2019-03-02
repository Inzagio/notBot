import asyncio
import discord
from discord.ext import commands

class CustomEvents:
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_message(self, message):
            print(message.content)
            
def setup(bot):
    bot.add_cog(CustomEvents(bot))