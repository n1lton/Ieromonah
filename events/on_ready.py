from discord.ext import commands
from database import DataBase
from config import cfg, roles
from time import time as getTime
from assets.mute import unmute
import discord, asyncio

db = DataBase()

async def unmuteAfter(member, sec):
    await asyncio.sleep(sec)
    await unmute(member)

async def on_ready():
    guild = botVar.get_guild(cfg["guild"])
    print(f"\nGuild: '{guild}'")

    for member in guild.members:
        if member.bot:
            continue

        print(member)

        db.cur.execute(f"SELECT mute FROM users WHERE id = {member.id}")
        data = db.cur.fetchone()

        if not data:
            memberLevel = 0
            for role in member.roles:
                if role.id in roles and roles.index(role.id) > memberLevel:
                    memberLevel = roles.index(role.id)

            db.cur.execute("INSERT INTO users (id, level) VALUES (?, ?)", (member.id, memberLevel))
            db.conn.commit()

        elif data[0]:
            unixTime = data[0]
            if unixTime - getTime() > 0:
                asyncio.create_task(unmuteAfter(member, unixTime - getTime()))
            else:
                await unmute(member)


def setup(bot: commands.Bot):
    global botVar; botVar = bot
    bot.__setattr__(on_ready.__name__, on_ready)