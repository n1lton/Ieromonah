import discord
from config import roles
from database import DataBase
from achivements.achivementManager import AchivementManager

manager = AchivementManager()
db = DataBase()


async def setLevel(member, level: int):
    if level is not None and (level >= len(roles) or level < 0):
        raise ValueError("Too low/big level value")


    db.cur.execute("UPDATE users SET level = ? WHERE id = ?", (level, member.id))
    db.conn.commit()

    await manager.check(member, 3)

    newRole = discord.utils.get(member.guild.roles, id=roles[level])
    oldRoles = []

    for role in member.roles:
        if role.id in roles and role != newRole:
            oldRoles.append(role)

    if oldRoles: await member.remove_roles(*oldRoles)
    if newRole not in member.roles: await member.add_roles(newRole)


