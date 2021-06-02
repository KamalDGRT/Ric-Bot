import logging
import discord


def create_logger():
    """Create a Logger"""

    logger = logging.getLogger("discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
                                  filename='discord.log',
                                  encoding='utf-8',
                                  mode='w'
                                  )
    handler.setFormatter(logging.Formatter(
                                           '%(asctime)s:'
                                           '%(levelname)s:'
                                           '%(name)s:'
                                           '%(message)s'
                                           ))
    logger.addHandler(handler)
    logger.addHandler(handler)
    return logger
