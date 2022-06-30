from discord.ext import commands
import discord


@commands.command(name="гигачад")
async def command(ctx: commands.Context):
    file = discord.File("gigachad.jpg")
    await ctx.reply(file=file)


def setup(bot: commands.Bot):
    bot.add_command(command)