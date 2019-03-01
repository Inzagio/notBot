import asyncio
import discord
import requests
from discord.ext import commands

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        r = requests.get('http://www.bzl.no/api/quotes.php')
        j = r.json()
        await ctx.send('{0} -- {1}'.format(j['text'], j['from']))
