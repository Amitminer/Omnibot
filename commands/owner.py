import discord
from discord.ext import commands
import json

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('owner cog loaded-----')

    conf = {}

    async def is_owner(ctx):
        global conf
        return ctx.message.author.id in conf["owner_id"]

    def __init__(self, client, config):
        self.client = client
        self.config = config
        global conf
        conf = config
        
    @commands.command(name='', hidden=True)
    @commands.is_owner()
    async def shutdown_bot(self, ctx):
        await ctx.send('Shutting down...')
        await self.client.close()
        
    @commands.command(name='reloadall', hidden=True)
    @commands.is_owner()
    async def reload_all(self, ctx):
       message = await ctx.send('Reloading...')
       await ctx.message.delete()
       try: 
               for cog in list('./cogs'):
                       if cog.endswith('.py') == True:
                               self.client.reload_extension(f'cogs.{cog[:-3]}')
       except Exception as exc:
               await message.edit(content=f'An error has occurred: {exc}', delete_after=20)
       else:
               await message.edit(content='All cogs have been reloaded.', delete_after=20)


def check_cog(self, cog):
    if (cog.lower()).startswith('cogs.') == True:
      return cog.lower()
    return f'cogs.{cog.lower()}'


async def setup(bot):
    await bot.add_cog(owner(bot, bot.config))