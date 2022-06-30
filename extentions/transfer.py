from discord.ext import commands
import discord
from database import DataBase
from assets.moneyFunc import plusMoney
from messages import showError
from config import cfg

db = DataBase()

@commands.command(name="перевод")
async def command(ctx, member: discord.Member, count: int):
    if member == ctx.author:
        await ctx.reply(embed=showError("Дэбил, нельзя перевести деньги самому себе"))
        return

    if member.bot:
        await ctx.reply(embed=showError("Дэбил, нельзя перевести деньги боту"))
        return

    if count < 1:
        await ctx.reply(embed=showError("Слишком маленькая сумма"))
        return

    db.cur.execute(f"SELECT money FROM users WHERE id = {ctx.author.id}")
    data = db.cur.fetchone()[0]

    if count > data:
        await ctx.reply(embed=showError("Слишком большая сумма"))
        return

    plusMoney(ctx.author.id, -count); plusMoney(member.id, count)
    embed = discord.Embed(
        title="Перевод",
        description=f"{ctx.author.mention} перевёл {count} <:gaycoin:955537976467808306> {member.mention}",
        color=cfg["color"]
    )
    await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_command(command)