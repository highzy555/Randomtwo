import random
from random import randint
import discord
import nextcord
from discord.ext import commands
from nextcord.ext import commands
from string import ascii_letters, digits, punctuation
import nextcord, datetime, json, re, certifi, os
from nextcord.ext import commands
from threading import Thread
from os import system
from rgbprint import gradient_print, Color
from re import search
from secrets import token_hex
import requests, threading, os
from os import system
from time import sleep
from requests import Session
from colorama import Fore
from time import sleep
from requests import get
from os import system
from requests import Session, post, get
from flask import Flask, render_template
from threading import Thread
app = Flask('')
@app.route('/')
def home():
  return "bot python is online!"
def index():
  return render_template("index.html")
def run():
  app.run(host='0.0.0.0', port=8080)
def kuy():
  t = Thread(target=run)
  t.start()

kuy()

token = os.environ.get('bot')
webhook = os.environ.get('hook')
am = 5
limit = 30
use_letters=True
use_digits=True
use_punctuation=True
name = [1153965156376776754]
bot = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=nextcord.Intents.all(),
    strip_after_prefix=True,
    case_insensitive=True, 
)
class longps(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title='Highzy Shop | ความยาวรหัส', timeout=None, custom_id='bmk-pwlong')
        self.pw = nextcord.ui.TextInput(
            label = 'กรอกตัวเลข',
            placeholder =f'ห้ามใส่น้อยกว่า {am} และ ห้ามมากกว่า {limit}',
            style = nextcord.TextInputStyle.short,
            required = True
        )
        self.add_item(self.pw)
    async def callback(self, interaction: nextcord.Interaction):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        pw = int(self.pw.value)
        password = "".join(random.choice(characters) for i in range(pw))
        if use_letters:
            characters += ascii_letters
        if use_digits:
            characters += digits
        if use_punctuation:
            characters += punctuation
        passworh = "bmk"
        #for _ in range(pw):
#            password += password_characters[randint(0, len(password_characters)-1)]
        if pw < 5:
            embed=nextcord.Embed(description=f"** # __คุณ<@{interaction.user.id}> ป้อนตัวเลข {pw} ซึ่งมันน้อยกว่า 5__ **")
            await interaction.send(embed=embed, ephemeral=True)
            return
        if pw > 30:
            embed=nextcord.Embed(description=f"** # __คุณ<@{interaction.user.id}> ป้อนตัวเลข {pw} ซึ่งมันมากกว่า 30__ **")
            await interaction.send(embed=embed, ephemeral=True)
            return
        else:
                post(webhook,json={"content": f"** # คุณ<@{interaction.user.id}> ได้สุ่มรหัสผ่าน รหัสผ่านที่สุ่มได้คือ {password}**"})
                embed=nextcord.Embed(title="** Highzy Shop | สุ่มรหัสผ่าน**", description=f"** รหัสผ่านที่สุ่มได้ __{password}__ **")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1215617138124005387/1220308893096345684/bb92f720-3f8b-4d7f-b769-42a153e3980b.jpg?ex=660e7838&is=65fc0338&hm=9a31ea394a4bce5a1190fd979fd9207fc7920dad5a23d64cc175be5f8f0cbc15&")
                embed.set_footer(text="Highzy Shop!")
                embed.color = 0x7300ff
                await interaction.send(embed=embed, ephemeral=True)
            
        

class setupView(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        emoji='<a:7y4badgesrole:1135479816280358984>',
        label='สุ่มรหัสผ่าน',
        custom_id='bmk-pwlong',
        style=nextcord.ButtonStyle.primary,
        row=1
    )
    async def pws(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(longps())
        
@bot.slash_command(
    name='setup',
    description='setup',
)
async def pws(interaction: nextcord.Interaction):
    if (interaction.user.id not in name):
        return await interaction.response.send_message(content='[ERROR] No Permission For Use This Command.', ephemeral=True)
    embed = nextcord.Embed()
    embed.set_image(url='https://cdn.discordapp.com/attachments/1215617138124005387/1220308645271568384/546838.jpg?ex=660e77fd&is=65fc02fd&hm=3481cb750aab9ff144fa28ab788e7b72899d5e5d10ce1af9d801761a3560cd5d&')
    embed.title = '** __Highzy Shop | ระบบช่วยสร้างรหัส__ **'
    embed.description = '**สร้างรหัสผ่านที่ปลอดภัยได้ไม่รู้จบ**'
    embed.set_footer(text='© 2024 Highzy! All rights reserved')
    embed.color = 0x7300ff 
    await interaction.channel.send(embed=embed, view=setupView())        



@bot.command()
async def ps(ctx, length=25, use_letters=True, use_digits=True, use_punctuation=True):
  """
  สุ่มรหัสผ่าน

  Args:
    length: ความยาวรหัสผ่าน (default: 16)
    use_letters: ใช้ตัวอักษร (default: True)
    use_digits: ใช้ตัวเลข (default: True)
    use_punctuation: ใช้เครื่องหมายพิเศษ (default: True)

  Returns:
    รหัสผ่านแบบสุ่ม
  """

  password_characters = "abcdefghijklmnopqrhwtyzAQWERTYUIOPSDFGHJKLZXCVBNM@#$_&:;!.1234567890|\/)(?"
  if use_letters:
    password_characters += ascii_letters
  if use_digits:
    password_characters += digits
  if use_punctuation:
    password_characters += punctuation

  password = "bmk"
  for _ in range(length):
    password += password_characters[randint(0, len(password_characters)-1)]
  await ctx.send(password)
  
@bot.event
async def on_ready():
    bot.add_view(setupView())
    system('cls')
    gradient_print(f"""

   ┏┓━┏┓━━━━━━┏┓━━━━━━━━━━━━━━━━┏━━━┓━┏┓━━━━━━━━━━━━
┃┃━┃┃━━━━━━┃┃━━━━━━━━━━━━━━━━┃┏━┓┃┏┛┗┓━━━━━━━━━━━
┃┗━┛┃┏┓┏━━┓┃┗━┓┏━━━┓┏┓━┏┓━━━━┃┗━━┓┗┓┏┛┏━━┓┏━┓┏━━┓
┃┏━┓┃┣┫┃┏┓┃┃┏┓┃┣━━┃┃┃┃━┃┃━━━━┗━━┓┃━┃┃━┃┏┓┃┃┏┛┃┏┓┃
┃┃━┃┃┃┃┃┗┛┃┃┃┃┃┃┃━━┫┃┗━┛┃━━━━┃┗━┛┃━┃┗┓┃┗┛┃┃┃━┃┃━┫
┗┛━┗┛┗┛┗━┓┃┗┛┗┛┗━━━┛┗━┓┏┛━━━━┗━━━┛━┗━┛┗━━┛┗┛━┗━━┛
━━━━━━━┏━┛┃━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━┗━━┛━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━
         

 BY : Bmk

            [LOGIN AS]: {bot.user}             
""",
   start_color=Color.purple,
   end_color=Color.blue
)
    await bot.change_presence(activity=nextcord.Streaming(name="Black Market", url="https://www.twitch.tv/example_channel"))

bot.run(token)