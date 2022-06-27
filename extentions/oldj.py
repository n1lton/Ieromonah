from discord.ext import commands

@commands.command(name="олдж")
async def command(ctx):
    await ctx.reply("ОЛДЖ УБИВАИТ")

def setup(bot: commands.Bot):
    bot.add_command(command)