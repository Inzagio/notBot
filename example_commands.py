import asyncio
import discord
from discord.ext import commands

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def noarg(self, ctx):
        await ctx.send('No argument list in signature')

    @commands.command()
    async def nullable(self, ctx, *args):
        await ctx.send('nullable arguments ({0}): {1}'.format(len(args), args))