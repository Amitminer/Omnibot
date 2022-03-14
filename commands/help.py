import discord
from discord.ext import commands


bot_title = 'Commands'
bot_description = 'my prefix is +'
bottom_info = 'made by Amit#4871'

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help',
                      description='Help command',
                      aliases=['info', 'commands'],
                      case_insensitive=True)
    async def help_command(self, ctx, *commands: str):
        bot = ctx.bot
        embed = discord.Embed(title=bot_title, description=bot_description)

        def generate_usage(command_name):
            temp = f'{prefix}'
            command = bot.get_command(command_name)
            if len(command.aliases) == 0:
                temp += f'{command_name}'
            elif len(command.aliases) == 1:
                temp += f'[{command.name}|{command.aliases[0]}]'
            else:
                t = '|'.join(command.aliases)
                temp += f'[{command.name}|{t}]'                
            params = f' '
            for param in command.clean_params:
                params += f'<{command.clean_params[param]}> '
            temp += f'{params}'
            return temp

        def generate_command_list(cog):
            max = 0
            for command in bot.get_cog(cog).get_commands():
                if not command.hidden:
                    if len(f'{command}') > max:
                        max = len(f'{command}')
            temp = ""
            for command in bot.get_cog(cog).get_commands():
                if command.hidden:
                    temp += ''
                elif command.help is None:
                    temp += f'{command}\n'
                else:
                    temp += f'`{command}`'
                    for i in range(0, max - len(f'{command}') + 1):
                        temp += '   '
                    temp += f'{command.help}\n'
            return temp

        if len(commands) == 0:
            for cog in bot.cogs:
                temp = generate_command_list(cog)
                if temp != "":
                    embed.add_field(name=f'**{cog}**', value=temp, inline=False)
            if bottom_info != "":
                embed.add_field(name="Info", value=bottom_info, inline=False)
        elif len(commands) == 1:
 
            name = commands[0].capitalize()
            command = None

            if name in bot.cogs:
                cog = bot.get_cog(name)
                msg = generate_command_list(name)
                embed.add_field(name=name, value=msg, inline=False)
                msg = f'{cog.description}\n'
                embed.set_footer(text=msg)

            else:
                command = bot.get_command(name)
                if command is not None:
                    help = f''
                    if command.help is not None:
                        help = command.help
                    embed.add_field(name=f'**{command}**',
                                    value=f'{command.description}```{generate_usage(name)}```\n{help}',
                                    inline=False)
                else:
                    msg = ' '.join(commands)
                    embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')
        else:
            msg = ' '.join(commands)
            embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')

        await ctx.send(f'{ctx.author.mention}', embed=embed)
        return


def setup(bot):
    bot.add_cog(help(bot))
