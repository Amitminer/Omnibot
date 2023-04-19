import discord
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('ping cog loaded-----')


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')


async def setup(bot):
    await bot.add_cog(ping(bot))