from discord.ext import commands
from database import DataBase
from config import cfg, roles, adminRoles
from time import time as getTime
from assets.mute import unmute, unmuteRoleAfter
import discord, asyncio, json

db = DataBase()


async def unmuteAfter(member, sec):
    await asyncio.sleep(sec)
    await unmute(member)


def unmuteRole(role, date, mode):
    difference = date - getTime()
    seconds = difference if difference >= 0 else 0
    asyncio.create_task(unmuteRoleAfter(role, seconds, mode))


def checkJsonData(guild):
    with open("cache.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if data["allMute"]:
        for roleId in roles:
            role = discord.utils.get(guild.roles, id=roleId)
            unmuteRole(role, data["allMute"], "allMute")

        if data["popushMute"]:
            data["popushMute"] = None
            with open("cache.json", "w", encoding="utf-8") as f:
                json.dump(data, f)

    elif data["popushMute"]:
        role = discord.utils.get(guild.roles, id=roles[1])
        unmuteRole(role, data["popushMute"], "allMute")


async def on_ready():
    guild = botVar.get_guild(cfg["guild"])
    checkJsonData(guild)
    
    print(f"\nGuild: '{guild}'")

    for member in guild.members:
        if member.bot:
            continue

        print(member)

        db.cur.execute(f"SELECT mute FROM users WHERE id = {member.id}")
        data = db.cur.fetchone()
        # data = '(None,)' or '(27349824792479,)' if member in database
        # and 'None' if not

        if not data:
            memberLevel = 0

            for role in member.roles:
                if role.id in adminRoles:
                    memberLevel = 6
                    break

                if role.id in roles and roles.index(role.id) > memberLevel:
                    memberLevel = roles.index(role.id)

            db.cur.execute("INSERT INTO users (id, level) VALUES (?, ?)", (member.id, memberLevel))
            db.conn.commit()


        elif data[0]: # if member is muted
            unixTime = data[0]
            if unixTime - getTime() > 0:
                asyncio.create_task(unmuteAfter(member, unixTime - getTime()))

            else:
                await unmute(member)


def setup(bot: commands.Bot):
    global botVar; botVar = bot
    bot.__setattr__(on_ready.__name__, on_ready)