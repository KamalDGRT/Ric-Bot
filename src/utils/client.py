"""
This module controls the Discord client behavior.

Classes: Discord
Functions: runClient()
"""

# Built-In Libraries/Modules/Packages
from os import listdir, getcwd
from os.path import dirname, join
from traceback import print_exc

# Third Party Libraries/Modules/Packages
from discord import ClientException
from discord.ext import commands

# User Defined Libraries/Modules/Packages
from .settings import loadSettings, runDiscordBot


class Discord(commands.Bot):
    """
    Discord bot client class.

    Methods:
        on_ready(self)
        loadCogs(self)
    """

    def __init__(self, command_prefix, help_command=None):
        super().__init__(command_prefix=command_prefix, help_command=help_command)
        self.loadCogs()

    async def on_ready(self):
        """Displays success message if connection is successful."""
        print("Logged on as", self.user)

    def loadCogs(self):
        """
        Loads the cogs that handles individual commands
        """

        # Getting the `moudles` directory's path
        cogs_dir = join(dirname(dirname(__file__)), "modules")

        # Getting all the python files present in `cogs` to a List
        pythonFiles = [
            File for File in listdir(cogs_dir) if File.endswith(".py")
        ]

        for File in pythonFiles:
            cog = File.replace('.py', '')
            try:
                self.load_extension(f'modules.{cog}')
            except (ClientException, ModuleNotFoundError):
                print(f'Failed to load extension {cog}.')
                print_exc()


def runClient():
    """
    This method loads the environment variables and runs the Discord bot client.
    """
    loadSettings()
    client = Discord(command_prefix="!", help_command=None)
    runDiscordBot(client)
