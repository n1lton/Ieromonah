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
        member = kwargs.get("member")
        db.cur.execute(f"SELECT level FROM users WHERE id = {member.id}")
        memberLevel = db.cur.fetchone()[0]
        await setLevel(member, memberLevel+1)

    @staticmethod
    async def getPrice(**kwargs):
        member = kwargs.get("member")
        db.cur.execute(f"SELECT level FROM users WHERE id = {member.id}")
        level = db.cur.fetchone()[0]

        return 100 * (level**2 + 1)
        




def setup(shop):
    item = ShopItem()
    shop.items[item.name] = item


