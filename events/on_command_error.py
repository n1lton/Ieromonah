from discord.ext import commands
import discord
from messages import showError
from database import DataBase
from random import randint
from config import roles, otherRoles

db = DataBase()

async def on_command_error(ctx: commands.Context, error: Exception):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(
            embed=showError(
                "IQ как у хлебушка додикп, ты пропустил один или несколько аргументов <:dol8ae8:849201617969479700>"
            )
        )

    elif isinstance(error, commands.BadArgument):
        await ctx.reply(
            embed=showError(
                "IQ как у хлебушка додикп, ты неправильно указал один или несколько аргументов <:dol8ae8:849201617969479700>"
            )
        )

    elif isinstance(error, commands.TooManyArguments):
        await ctx.reply(
            embed=showError(
                "IQ как у хлебушка додикп, зоч так много аргументов? <:obobo:954997386550321182>"
            )
        )

    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction("🐔")

    else:
        await ctx.reply(
            embed=showError(f"Произошёл какой-то прикол\n{error}")
        )
        

def setup(bot: commands.Bot):
    bot.__setattr__(on_command_error.__name__, on_command_error)