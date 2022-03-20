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

    async def cog_check(self, ctx):
        gerants = discord.utils.get(ctx.guild.roles, id = 889167189830160414)
        return gerants in ctx.author.roles

    async def cog_check(self, ctx):
        responsable = discord.utils.get(ctx.guild.roles, id = 889168031647928370)
        return responsable in ctx.author.roles

    async def cog_check(self, ctx):
        secretaire = discord.utils.get(ctx.guild.roles, id = 889176817284562945)
        return secretaire in ctx.author.roles

#    async def cog_check(self, ctx):
#        super_modo = get(ctx.guild.roles, id = 904482032430755911)
#        return super_modo in ctx.author.roles 

#    async def cog_check(self, ctx):
#        modo = get(ctx.guild.roles, id = 889168519114158132)
#        return modo in ctx.author.roles 
    
    @commands.command()
    async def join(self, ctx):
        #gerant = discord.utils.get(ctx.guild.roles, id = 889167189830160414)
        channel = ctx.author.voice.channel
        await ctx.send('Joined !')
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.send('Leaved !')
        await ctx.voice_client.disconnect()

def setup(bot: commands.Bot):
    bot.add_cog(Voc(bot))