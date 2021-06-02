"""
This module contains settings and configurations for the bot.

Classes: 
    Settings
Functions: 
    loadReddit()
    loadSettings()
    getSubreddits()
    getPostLimit()
    runDiscordBot()
"""


import os
import discord
from os.path import join
from dotenv import load_dotenv
from asyncpraw import Reddit


class Settings:
    """
    Abstract entity to hold the settings for the bot.

    Methods:
        _getSecrets(self)
    """

    _BOT_NAME = "Ric-Bot - Discord bot by Tesseract Coding"
    _SUBREDDITS = "funnyterriblefacebookmemes+wholesomememes+ProgrammerHumor+MemeEconomy+memes+AdviceAnimals+sfwmemes+BikiniBottomTwitter"
    _POST_LIMIT = 21  # WARNING - AVOID CHANGING THIS!!!
    SECRETS = {"DISCORD_TOKEN": "", "REDDIT_CLIENT_ID": "", "REDDIT_CLIENT_SECRET": ""}

    def _getSecrets(self) -> None:
        """Fetches information from env variables into the object."""
        try:
            for i in self.SECRETS:
                self.SECRETS[i] = os.environ[i]
        except:
            return "Error in loading environment variables."  # take this check to the loadSettings() function.


def loadReddit() -> Reddit:
    """Performs the connection to the Reddit API"""
    reddit = Reddit(
        client_id=Settings.SECRETS["REDDIT_CLIENT_ID"],
        client_secret=Settings.SECRETS["REDDIT_CLIENT_SECRET"],
        user_agent=Settings._BOT_NAME,
    )
    return reddit


def loadSettings() -> None:
    """
    Loads environment variables into the module and object.

    This is a bit of a Frankenstein that definitely needs to be changed.
    First, it loads the environment variables, then it creates the object
    and then loads the env variable values into it.

    This fix should be easy, and if you are reading this and thinks you
    can do it, maybe you should.
    """
    # to be changed - add a try/catch for the .env file
    dotenv_path = join(os.getcwd(), ".env")
    load_dotenv(dotenv_path)
    settings = Settings()
    Settings._getSecrets(settings)


def getSubreddits() -> str:
    """Returns subreddit list."""
    return Settings._SUBREDDITS


def getPostLimit() -> int:
    """Returns post limit for meme generator."""
    return Settings._POST_LIMIT


def runDiscordBot(DiscordClient: discord.Client) -> None:
    """Runs the discord client."""
    discord = DiscordClient
    discord.run(Settings.SECRETS["DISCORD_TOKEN"])
