import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv #remove this line if you are using replit 
from keep_alive import keep_alive

load_dotenv() #remove this line if you are using replit 

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

prefix = config["Prefix"]

client = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=False)
client.config = config

cogs = ["commands.owner", "commands.ping", "commands.help", "commands.say"]

@client.event
async def on_ready():#loading bot and status
    print('Logged in as')
    print(client.user.name)
    print('Made by Amit')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="github.com/Amitminer888", type=discord.ActivityType.watching))     
for cog in cogs:                          
    try: 
      client.load_extension(cog)           
      print("commands was loaded.")       
    except Exception as e:
      
      print(e)

keep_alive()
TOKEN = os.getenv("BOT_TOKEN")
client.run(TOKEN)
