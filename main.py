import discord
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv
from os import getenv
load_dotenv()

intents = discord.Intents.default() 
intents.members = True

bot = commands.Bot(command_prefix='!lp', intents = intents)
slash = SlashCommand(bot, sync_commands = True)

bot.load_extension('Bienvenue.bienvenue')
bot.load_extension('Voc.role-voc')
bot.load_extension('Voc.voc')

@bot.event
async def on_ready():
    print('Lancé !')

@bot.command()
async def coucou(ctx):
    await ctx.reply('Coucou !')


























































bot.run(getenv('TOKEN'))