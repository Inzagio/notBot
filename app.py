import discord
import asyncio
import config
from discord.ext import commands

# from commandsModule import CommandsTest

client = discord.Client()

bot = commands.Bot(command_prefix='!')   

@bot.command()
async def what(ctx):
    pass


@bot.command()
async def testArgs(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))


@client.event # event decorator/wrapper
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content} ")
    
    if "hi there" in message.content.lower():
        await message.channel.send(f"Hi! {message.author.name}")


client.run(config.token)
