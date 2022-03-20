import discord
from discord.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.reply(f'Pong!\n{round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(PingCog(bot))