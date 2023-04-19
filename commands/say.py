import discord
from discord.ext import commands

class say(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('say cog loaded-----')


    @commands.command()
    async def say(self, ctx, *, text=''):
        if text == '':
            await ctx.send("You need to say something")
        else:
            await ctx.send(text)

async def setup(client):
    await client.add_cog(say(client))
