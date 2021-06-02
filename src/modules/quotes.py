"""
This module implements the random quote generator.

Classes: Quotes
Functions: 
    getQuote()
    setup(client)
"""
# Built-In Libraries/Modules/Packages
from json import loads
import random

# Third Party Libraries/Modules/Packages
from discord import Embed, Color
from discord.ext import commands
from urllib.request import urlopen


class Quotes(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command(
        name='quote'
    )
    async def sendQuote(self, ctx):
        """
        A user defined async function that returns a
        random quote as an Embed object.
        """

        message = getQuote()

        embed = Embed(
            title=message['quote'],
            color=Color.blurple()
        )

        embed.set_footer(
            text=message['author']
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Quotes(client))


def getQuote() -> dict:
    """
    Fetches a random quote from an API, and returns a
    dictionary containing quote and its author.
    """
    response = urlopen('https://zenquotes.io/api/random')
    data = response.read()
    jsonData = loads(data)

    return {
        "quote": str(jsonData[0]['q']),
        "author": str(jsonData[0]['a'])
    }
