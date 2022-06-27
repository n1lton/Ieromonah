from database import DataBase
import discord

db = DataBase()

def plusMoney(memberId: int, money: int):
    db.cur.execute("UPDATE users SET money = money + ? WHERE id = ?", (money, memberId))
    db.conn.commit()