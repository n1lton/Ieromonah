from discord.ext import commands

class Ieromonah:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
           cls.__instance = commands.Bot(*args, **kwargs)
        return cls.__instance