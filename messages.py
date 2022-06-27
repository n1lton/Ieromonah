import discord
from config import cfg
import asyncio

def showError(err: str):
    embed = discord.Embed(
        title="Ошибка",
        description=err,
        color=cfg["color"]
    )
    return embed

def showMessage(msg: str):
    embed = discord.Embed(
        title="Сообщение",
        description=msg,
        color=cfg["color"]
    )
    return embed

async def ephemeralError(ctx, err: str):
    msg = await ctx.message.reply(embed=showError(err))
    await asyncio.sleep(10)
    await ctx.message.delete()
    await msg.delete()
