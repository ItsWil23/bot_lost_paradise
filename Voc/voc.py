import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from os import getenv
load_dotenv()

intents = discord.Intents.default() 
intents.members = True

class Voc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role(889167189830160414, 889168031647928370, 904482032430755911)      #Gérants, Responsables, Super-modo
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await ctx.send('Joined !')
        await channel.connect()

    @commands.command()
    @commands.has_any_role(889167189830160414, 889168031647928370, 904482032430755911)      #Gérants, Responsables, Super-modo
    async def leave(self, ctx):
        await ctx.send('Leaved !')
        await ctx.voice_client.disconnect()

def setup(bot: commands.Bot):
    bot.add_cog(Voc(bot))