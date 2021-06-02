from discord.ext import commands

# Dictionary that tracks the frequency of the commands executed.
commands_tally = {}

"""
This module implements the command events of the bot.
It listens to some of the events and keeps track of
the commands executed.
"""


class Commands(commands.Cog):

    # The constructor 
    def __init__(self, bot):
        self.bot = bot

    '''
    Command Error, Successful, Invocation Handling
    '''

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + ' was invoked correctly.')
        print(error)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:
            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1
            print(commands_tally)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name + ' was invoked successfully.')

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(Commands(bot))
