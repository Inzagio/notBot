import discord
import asyncio
import config
from discord.ext import commands
from custom_commands import CustomCommands

bot = commands.Bot(command_prefix='$')

bot.load_extension("cogs.events")
bot.load_extension("cogs.commands")

bot.run(config.token)

# bot.change_presence(activity=discord.Game(name='World of Bots'))
