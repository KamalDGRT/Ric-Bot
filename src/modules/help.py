from discord.ext import commands
"""
This module implements the help command for the bot.

Classes: Help
Functions: 
    help()
    setup(client)
"""


class Help(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def help(self, ctx):
        """Handles help command"""
        await ctx.send(help())


def help() -> str:
    """
    Returns the command list as a string.
    """

    return """
commands
    !help:\t Help menu
    !ping:\t Replies with pong and latency
    !memes:\t Fetchs a random meme from reddit
    !quote:\t Displays a quote
"""


def setup(client):
    client.add_cog(Help(client))
