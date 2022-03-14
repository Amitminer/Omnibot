import discord
from discord.ext import commands

class say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, text=''):
        if text == '':
            await ctx.send("You need to say something")
        else:
            await ctx.send(text)
   
def setup(client):
    client.add_cog(say(client))
