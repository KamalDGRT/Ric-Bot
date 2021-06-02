"""
This module implements the random meme generator.

Classes: Memes
Function: 
    get_memes()
    setup(client)
"""
import random
from utils.settings import loadReddit, getPostLimit, getSubreddits
from discord.ext import commands


class Memes(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def memes(self, ctx):
        """Handles memes command"""
        await ctx.send(await get_memes())


def setup(client):
    client.add_cog(Memes(client))


async def get_memes() -> str:
    """
    Fetches random meme from Reddit and returns URL of the image.

    This module fetches a random meme from the 21(*) hottest posts
    from a list of subreddits(*), extracts the URL image from it
    and then returns it as a string to be sent as a message to Discord.

    Returns: Image URL of random meme from Reddit.
    """
    reddit = loadReddit()
    postLimit = getPostLimit()
    subreddit = await reddit.subreddit(getSubreddits())
    posts = subreddit.hot(limit=postLimit)
    image_urls, image_titles = [], []

    async for post in posts:
        image_urls.append(post.url.encode("utf-8"))
        image_titles.append(post.title.encode("utf-8"))

    image_urls = [i.decode() for i in image_urls]

    return image_urls[random.randint(0, postLimit - 1)]
