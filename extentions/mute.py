from discord.ext import commands
import discord, asyncio
from pytimeparse import parse
from time import time as getTime
from database import DataBase
from messages import showError
from typing import Optional
from database import DataBase
from config import otherRoles, cfg
from assets.mute import mute, unmute


db = DataBase()


@commands.slash_command(name="мут", description="мутит челика на какое-то время в формате '1w 1d 1h 1m 1s'")
async def command(ctx, member: discord.Member, time: str = "1h", reason: Optional[str] = "Не указана"):
    if not ctx.author.guild_permissions.mute_members:
        await ctx.respond(
            embed=showError("Нет прав"),
            ephemeral=True
        )

    try: # time parsing
        unixTime = parse(time)
    except:
        await ctx.respond(
            embed=showError("Неправильный формат времени"),
            ephemeral=True
        )
        return

    if unixTime > 60*60*24*6: # 6 month
        await ctx.respond(
            embed=showError("Слишком большое время мута"),
            ephemeral=True
        )
        return
    
    # if member is muted already
    db.cur.execute(f"SELECT mute FROM users WHERE id = {member.id}") 
    if db.cur.fetchone()[0] is not None:
        await ctx.respond(
            embed=showError("Участник уже в муте"),
            ephemeral=True
        )
        return

    await mute(ctx, member, unixTime, reason)
    
    

def setup(bot: commands.Bot):
    bot.add_application_command(command)