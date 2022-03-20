import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class RoleVoc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()   
    async def on_voice_state_update(self, member, before, after):
        if member.id == 915683208480321616:
            return

        if not before.channel and after.channel:
            member = member
            role = discord.utils.get(member.guild.roles, id = 912106048452706425) #id du rôle "En voc"
            await member.add_roles(role) #rôle "En voc" est donné quand une voc est rejoint
        
        elif before.channel and not after.channel:
            member = member
            role = discord.utils.get(member.guild.roles, id = 912106048452706425) #id du rôle "En voc"
            await member.remove_roles(role) # rôle "En voc" est retiré quand une voc est quitté

def setup(bot: commands.Bot):
    bot.add_cog(RoleVoc(bot))