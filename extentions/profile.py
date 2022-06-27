from discord.ext import commands
import discord
from typing import Optional
from config import cfg, roles
from database import DataBase

@commands.command(name="профиль")
async def command(ctx: commands.Context, member: Optional[discord.Member]):
    if ctx.message.reference:
        msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        member = msg.author

    elif not member:
        member = ctx.author

    if member.bot:
        embed = discord.Embed(
            title=f"Профиль {member.nick if member.nick else member.name}",
            description="Это бот :) У него нет профиля.",
            color=cfg["color"]
        )
    else:
        db = DataBase()
        db.cur.execute(f"SELECT money, messages, text, level FROM users WHERE id = {member.id}")
        data = db.cur.fetchone()
        embed = discord.Embed(
            title=f"Профиль {member.nick if member.nick else member.name}",
            description = data[2],
            color=cfg["color"]
        )
        embed.add_field(
            name="Гейкойны",
            value=f"{data[0]}  <:gaycoin:955537976467808306>"
        ).add_field(
            name="Сообщения",
            value=data[1]
        ).add_field(
            name="Роль",
            value=f"{discord.utils.get(member.guild.roles, id=roles[data[3]]).name} / ☦🛐ПОЛУБОГ🛐☦\n({data[3]} / 5)",
            inline=False
        ).add_field(
            name="Id",
            value=member.id,

        )

        if member.avatar: embed.set_thumbnail(url=member.avatar.url)

    await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_command(command)