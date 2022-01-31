import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import colorama
from colorama import Fore
import asyncio

import os

prefix = "+" 

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=False)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game('example bot xD Amit OP'))
  print('Bot Is Online xD')

@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round (bot.latency * 1000)}ms')

@bot.command()
async def test(ctx):
  await ctx.send(f'test')
  
@bot.command()
async def help(ctx):
  embed = discord.Embed(title="commands", color=420699, description=f"**+ping**\nping command.\n\n**+say**\nsay command.")
  embed.set_image(url="https://cdn.discordapp.com/emojis/937399473636802580.gif")
  await ctx.send(embed=embed)
  
@bot.command()
async def say(ctx, *, message):
    try:
       await ctx.send(message)
    except:
       await ctx.send("Please Give Some Message!")
  
bot.run('token here')
