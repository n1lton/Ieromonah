from database import DataBase
import discord, asyncio
from config import cfg, otherRoles
from time import time as getTime

db = DataBase()

async def unmute(member: discord.Member):
    db.cur.execute("UPDATE users SET mute = ? WHERE id = ?", (None, member.id))
    db.conn.commit()

    role = discord.utils.get(member.guild.roles, id=otherRoles["mute"])

    if role in member.roles:
        await member.remove_roles(role)


async def mute(ctx, member: discord.Member, time: int, reason: str = "Не указана"):
    db.cur.execute("UPDATE users SET mute = ? WHERE id = ?", (time + getTime(), member.id))
    db.conn.commit()

    role = discord.utils.get(member.guild.roles, id=otherRoles["mute"])
    await member.add_roles(role)

    embed = discord.Embed(
            title="Мут",
            description=f"{ctx.author.mention} замутил {member.mention} на {time} секунд",
            color=cfg["color"]
    ).add_field(
        name="Истекает",
        value=f"<t:{int(getTime() + time)}:f>"
    ).add_field(
        name="Причина",
        value=reason,
        inline=False
    )

    if isinstance(ctx, discord.ext.commands.Context):
        await ctx.reply(embed=embed)
    else:
        await ctx.respond(embed=embed)

    await asyncio.sleep(time)
    await unmute(member)