from achivements.achivementClass import Achivement
import discord
from database import DataBase
from achivements.achivementManager import AchivementManager

db = DataBase()

# 100 сообщений
ach100 = Achivement(
    "100 Сообщений",
    1,
    "Написать 100 сообщений ✉️",
    0
)

@ach100.setCheck
async def check(member: discord.Member):
    messages = db.cur.execute(f"SELECT messages FROM users WHERE id = {member.id}").fetchone()[0]
    if messages >= 100:
        return True


# 1000 сообщений
ach1000 = Achivement(
    "10000 Сообщений",
    2,
    "Написать 1000 сообщений ✉️",
    1
)

@ach1000.setCheck
async def check(member: discord.Member):
    messages = db.cur.execute(f"SELECT messages FROM users WHERE id = {member.id}").fetchone()[0]
    if messages >= 10000:
        return True


# 10000 сообщений
ach10000 = Achivement(
    "10000 Сообщений",
    3,
    "Написать 10000 сообщений ✉️",
    2
)

@ach10000.setCheck
async def check(member: discord.Member):
    messages = db.cur.execute(f"SELECT messages FROM users WHERE id = {member.id}").fetchone()[0]
    if messages >= 10000:
        return True



def setup(manager: AchivementManager):
    manager.addAchivement(ach100)
    manager.addAchivement(ach1000)
    manager.addAchivement(ach10000)