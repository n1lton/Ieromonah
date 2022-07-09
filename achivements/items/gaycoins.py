from achivements.achivementClass import Achivement
import discord
from database import DataBase
from achivements.achivementManager import AchivementManager

db = DataBase()

# 100 гейкойнов
gc100 = Achivement(
    "100 Гейкойнов",
    1,
    "Накопить 100 Гейкойнов <:gaycoin:955537976467808306>",
    5
)
@gc100.setCheck
async def check(member: discord.Member):
    gaycoins = db.cur.execute(f"SELECT money FROM users WHERE id = {member.id}").fetchone()[0]
    if gaycoins >= 100:
        return True


# 100 гейкойнов
gc1000 = Achivement(
    "1000 Гейкойнов",
    2,
    "Накопить 1000 Гейкойнов <:gaycoin:955537976467808306>",
    6
)
@gc1000.setCheck
async def check(member: discord.Member):
    gaycoins = db.cur.execute(f"SELECT money FROM users WHERE id = {member.id}").fetchone()[0]
    if gaycoins >= 1000:
        return True


# 10000 гейкойнов
gc10000 = Achivement(
    "10000 Гейкойнов",
    3,
    "Накопить 10000 Гейкойнов <:gaycoin:955537976467808306>",
    7
)
@gc10000.setCheck
async def check(member: discord.Member):
    gaycoins = db.cur.execute(f"SELECT money FROM users WHERE id = {member.id}").fetchone()[0]
    if gaycoins >= 10000:
        return True


def setup(manager: AchivementManager):
    manager.addAchivement(gc100)
    manager.addAchivement(gc1000)
    manager.addAchivement(gc10000)