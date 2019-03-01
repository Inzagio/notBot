import discord
import asyncio
import config
from discord.ext import commands
from custom_commands import CustomCommands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(CustomCommands(bot))
bot.run(config.token)
