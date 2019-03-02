import discord
import asyncio
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

bot.load_extension("cogs.events")
bot.load_extension("cogs.commands")

bot.run(config.token)
