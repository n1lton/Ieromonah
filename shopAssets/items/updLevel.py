from urllib import response
from assets.role import setLevel
import discord
from database import DataBase
from config import roles
from shopAssets.baseShopItem import BaseShopItem

db = DataBase()

class ShopItem(BaseShopItem):
    name = "Повышение роли"
    description = "Повышает твою роль. Цена с каждым разом всё выше и выше."
    price = None

    @staticmethod
    async def check(**kwargs):
        member = kwargs.get("member")
        db.cur.execute(f"SELECT level FROM users WHERE id = {member.id}")
        level = db.cur.fetchone()[0]
        if level + 1 == len(roles):
            return "Ошибка: роль улучшена до максимума"
        return None

    @staticmethod
    async def func(**kwargs):
        ctx = kwargs.get("ctx")
        db.cur.execute(f"SELECT level FROM users WHERE id = {ctx.author.id}")
        memberLevel = db.cur.fetchone()[0]
        await setLevel(ctx.author, memberLevel+1)

    @staticmethod
    async def getPrice(**kwargs):
        member = kwargs.get("member")
        db.cur.execute(f"SELECT level FROM users WHERE id = {member.id}")
        level = db.cur.fetchone()[0]

        if level == len(roles) - 1:
            return "Нет"
        return 300 * (level**3 + 1)
        

def setup(shop):
    item = ShopItem()
    shop.items[item.name] = item


