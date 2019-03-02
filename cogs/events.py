from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        if "wow" in message.content:
            await message.add_reaction('\U0001F1F3')
            await message.add_reaction('\U0001F1EA')
            await message.add_reaction('\U0001F1F7')
            await message.add_reaction('\U0001F1E9')

def setup(bot):
    bot.add_cog(Events(bot))