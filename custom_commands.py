import asyncio
import discord
import aiohttp
from discord.ext import commands

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://www.bzl.no/api/quotes.php') as r:
                if r.status == 200:
                    json = await r.json()
                    await ctx.send('{0} -- {1}'.format(json['text'], json['from']))
        # r = requests.get('http://www.bzl.no/api/quotes.php')
        # j = r.json()
        # await ctx.send('{0} -- {1}'.format(j['text'], j['from']))

    @commands.command()
    async def pm(self, ctx):
        await ctx.message.author.send('Hi there')

    @commands.command()
    async def automate(self, ctx):
        await ctx.message.author.send('https://automatetheboringstuff.com/')