import imp
from discord.ext import commands
from config import cfg
from database import DataBase
from achivements.achivementManager import AchivementManager
import discord

db = DataBase()
manager = AchivementManager()

@commands.command(name="молитва")
async def command(ctx):
    db.cur.execute(f"UPDATE stats SET prayer = prayer + 1 WHERE id = {ctx.author.id}")
    db.conn.commit()

    embed = discord.Embed(
        title="Молитва",
        description=f"{ctx.author.mention} помолился 💪",
        color=cfg["color"]
    ).set_image(url="https://cdn.discordapp.com/attachments/765783278716059672/994947761298485269/Giga_chad_2.gif")

    await ctx.reply(embed=embed)
    await manager.check(ctx.author, 8)

def setup(bot: commands.Bot):
    bot.add_command(command)