import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import MemberConverter
import colorama
from colorama import Fore
import asyncio
from keep_alive import keep_alive

load_dotenv()

prefix = "+" 

client = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=False)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('example bot xD Amit OP'))
  print('Bot Is Online xD')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

@client.command()
async def test(ctx):
  await ctx.send(f'test')
  
@client.command()
async def help(ctx):
  embed = discord.Embed(title="commands", color=420699, description=f"**+ping**\nping command.\n\n**+say**\nsay command.")
  embed.set_image(url="https://cdn.discordapp.com/emojis/937399473636802580.gif")
  await ctx.send(embed=embed)
  
@client.command()
async def say(ctx, *, message):
    try:
       await ctx.send(message)
    except:
       await ctx.send("Please Give Some Message!")

keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
