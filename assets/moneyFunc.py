from database import DataBase
import discord
from achivements.achivementManager import AchivementManager

db = DataBase()
manager = AchivementManager()

async def plusMoney(member: discord.Member, money: int):
    db.cur.execute("UPDATE users SET money = money + ? WHERE id = ?", (money, member.id))
    db.conn.commit()
    await manager.check(member, 5, 6, 7)
