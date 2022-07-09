from discord.ext import commands
from achivements.achivementManager import AchivementManager
import discord

manager = AchivementManager()

@commands.command(name="гигачад")
async def command(ctx: commands.Context):
    file = discord.File("gigachad.jpg")
    await ctx.reply(file=file)
    await manager.check(ctx.author, 4)


def setup(bot: commands.Bot):
    bot.add_command(command)