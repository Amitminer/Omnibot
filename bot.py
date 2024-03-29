import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

with open('./config.json', 'r', encoding='utf-8') as cjson:
    config = json.load(cjson)

prefix = config["Prefix"]
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=prefix,
                      help_command=None,
                      case_insensitive=True,
                      self_bot=False, intents=intents)
client.config = config

cogs = ["commands.owner", "commands.ping", "commands.help",
        "commands.say", "commands.snap", "commands.ship"]


@client.event
async def on_ready():
    """
    This function is called when the bot is successfully logged in.
    It sets the bot's status and loads command extensions.
    """
    print('Logged in as')
    print(client.user.name)
    print('Made by Amit')
    await client.change_presence(status=discord.Status.dnd,
                                 activity=discord.Activity(name="github.com/Amitminer", type=discord.ActivityType.watching))
    for cog in cogs:
        try:
            await client.load_extension(cog)
            print("Commands loaded.")
        except Exception as e:
            print(e)


@client.command()
async def geturl(ctx, emoji: discord.Emoji):
    """
    Sends the URL of the provided emoji.
    Args:
        emoji (discord.Emoji): The emoji to get the URL for.
    """
    await ctx.send(emoji.url)

if __name__ == '__main__':
    keep_alive()
    TOKEN = os.getenv("BOT_TOKEN")
    client.run(TOKEN)