from achivements.achivementClass import Achivement
import discord
from database import DataBase
from achivements.achivementManager import AchivementManager

db = DataBase()


topRole = Achivement(
    "Почти Бог",
    3,
    "Получить роль 'ПОЛУБОГ'",
    3
)

@topRole.setCheck
async def check(member: discord.Member):
    db.cur.execute(f"SELECT level FROM users WHERE id = {member.id}")
    level = db.cur.fetchone()[0]

    if level == 5:
        return True


def setup(manager: AchivementManager):
    manager.addAchivement(topRole)
