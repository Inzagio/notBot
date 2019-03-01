from discord.ext import commands
import asyncio

class CommandsTest:
    pass

bot = commands.Bot(command_prefix='!')   

@bot.command()
async def what(ctx):
    pass

@bot.command()
async def testArgs(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))
