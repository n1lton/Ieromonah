from pydoc import describe
from discord.ext import commands
from config import cfg, chances
from random import randint
from database import DataBase
from assets.moneyFunc import plusMoney
import discord

db = DataBase()

@commands.command(name="копать")
async def command(ctx):
    if ctx.channel.id != cfg["mineChannel"]:
        return

    level = db.cur.execute(f"SELECT level FROM users WHERE id = {ctx.author.id}").fetchone()[0]

    if randint(0, 100) < chances[level]:
        win = randint(5, 30)
        plusMoney(ctx.author.id, win)
        msg=f"Легейнда, ти намайнил {win} <:gaycoin:955537976467808306>\nШансы на успех были {chances[level]}%"

    else:
        msg=f"Пхпхпх ыы обвалился олдж. Иди откисай))\nШансы на успех были {chances[level]}%"

    await ctx.reply(embed=discord.Embed(
        title="Шахта",
        description=msg,
        color=cfg["color"]
    ))


def setup(bot: commands.Bot):
    bot.add_command(command)