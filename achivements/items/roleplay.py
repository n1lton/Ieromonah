from pkg_resources import set_extraction_path
from achivements.achivementClass import Achivement
from database import DataBase

db = DataBase()

prayer = Achivement(
    "Священник-гигачад",
    2,
    "Помолиться 100 раз",
    8
)

@prayer.setCheck
async def check(member):
    count = db.cur.execute(f"SELECT prayer FROM stats WHERE id = {member.id}").fetchone()[0]
    if count >= 100:
        return True


sex = Achivement(
    "Лолька в подвале",
    3,
    "Паебаца 1 раз",
    9
)

@sex.setCheck
async def check(member):
    return True


def setup(manager):
    manager.addAchivement(prayer)
    manager.addAchivement(sex)