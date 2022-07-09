from assets.role import setLevel
from discord.ext import commands
from messages import showError
from config import roles, cfg
import discord

@commands.slash_command(name="уровень", description="Админ команда. Устанавливает роль по уровню (0 - неопред, 1 - попущ, ... 5 - полубог)")
async def command(ctx: commands.Context, member: discord.Member, level: int):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond(
            embed=showError("Нет прав"),
            ephemeral=True
        )
        return


    if 0 > level or level >= len(roles):
        await ctx.respond(
            embed=showError(f"Некорректный уровень (мин 0, макс {len(roles)-1})"),
            ephemeral=True
        )
        return

    elif not member:
        member = ctx.author

    if member.bot:
        await ctx.respond(
            embed=showError("У ботов нет уровней"),
            ephemeral=True
        )
        return

    await setLevel(member, level)
    await ctx.respond(
        embed=discord.Embed(
            title="Уровень",
            description=f"{ctx.author.mention} выдал {member.mention} {level} уровень",
            color=cfg["color"]
        )
    )


def setup(bot: commands.Bot):
    bot.add_application_command(command)