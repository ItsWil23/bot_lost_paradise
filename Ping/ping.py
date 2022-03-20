import discord
from discord.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return ctx.author.id == 737084050753323119

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.reply(f'Pong!\n{round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(PingCog(bot))