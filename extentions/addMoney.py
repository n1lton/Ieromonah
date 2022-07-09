from discord.ext import commands
from assets.moneyFunc import plusMoney
from config import cfg
from messages import showError
import discord

@commands.slash_command(name="пополнить", description="Увеличить число денег у челикпа. Можно ввести отрицательное значение")
async def command(ctx, member: discord.Member, num: int):
    if not ctx.author.guild_permissions.administrator:
        await ctx.respond(
            embed=showError("Нет прав"),
            ephemeral=True
        )
        return

    await plusMoney(member, num)
    await ctx.respond(
        embed=discord.Embed(
            title="Пополнение",
            description=f"{ctx.author.mention} добавил к деньгам {member.mention} {num} <:gaycoin:955537976467808306>",
            color=cfg["color"]
        )
    )

def setup(bot: commands.Bot):
    bot.add_application_command(command)