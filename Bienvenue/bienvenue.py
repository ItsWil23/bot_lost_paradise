import os
import requests
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Cog
from PIL import Image, ImageFont, ImageDraw, ImageChops
from io import BytesIO
import numpy as np

intents = discord.Intents.default() 
intents.members = True

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
#    @commands.Cog.listener()
#    async def on_member_join(self, member):        
    @commands.command()
    async def w(self, ctx, member: discord.Member = None):

        if member == None:
            member = ctx.author

        filename = 'image-bienvenue1.png'

        img_b = Image.open('/app/Bienvenue/bienvenue1.png')

       # userAvatarUrl = member.avatar_ur

        with requests.get(userAvatarUrl) as r:
            img_data = r.content
        with open('profile.jpg', 'wb') as handler:
            handler.write(img_data)
        asset = Image.open("profile.jpg")
        asset = asset.resize((1024, 1024), resample=0)

        pfp = circle(asset)
        pfp = pfp.resize((160,160))

        font_b = ImageFont.truetype('/app/Bienvenue/Cream-Cake.ttf', 100)                 #font pour bienvenue
        font_n = ImageFont.truetype('/app/Bienvenue/Please-write-me-a-song.ttf', 40)      #font pour le nom
        
        draw = ImageDraw.Draw(img_b)
        bienvenue = 'Bienvenue'
        user = member.name
        tag = member.discriminator
        nom = user + f'#{tag}'

        draw.ellipse((243, 12, 417, 187), fill = '#ce4e4d', outline ='#ce4e4d')
        img_b.paste(pfp, (250, 20), pfp)
        draw.text((325, 210), bienvenue, (0, 64, 128), anchor='mm', font=font_b)         #affichage de bienvenue
        draw.text((325, 270), nom, (0, 64, 128), anchor='mm', font=font_n)               #affichade du nom

        img_b.save(filename)

        channel_id = 889222155148079155
        channel = self.bot.get_channel(channel_id)
        file = discord.File(filename)
        msg = await channel.send('**<@&892846720327770122>''\r\n'f'Bienvenue {member.mention} sur __{member.guild.name}__ !''\r\n'f"N'hésites pas à prendre tes rôles dans :"'\r\n'
        f'> ➥ <#889610595370926121>''\r\n'f'> ➥ <#889731351501213756>''\r\n'f'Après ça viens discuter avec les autres, et trouver ta place au sein de notre communauté !''\r\n'
        f'━━━━━━━ ✗ ━━━━━━━**', file = file)
        await asyncio.sleep(1)

        try: 
            os.remove(filename)
        except:
            pass

def circle(pfp, size = (215,215)):

    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")

    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))