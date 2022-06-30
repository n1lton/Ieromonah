from database import DataBase
from shopAssets.baseShopItem import BaseShopItem
import discord, json, asyncio
from config import otherRoles
from assets.mute import unmuteRoleAfter
from time import time as getTime
from config import roles

db = DataBase()

class ShopItem(BaseShopItem):
    name = "Мут всех попущей на 30 минут"
    description = "Изменяет разрешения роли Божий Апущенка, запрещая писать сообщения."
    accessLevel = 2
    price = 1000

    @staticmethod
    async def check(**kwargs):
        with open("cache.json", "r", encoding="utf-8") as f:
            if json.load(f)["popushMute"]:
                return "Ошибка: кто-то уже замутил попущей"
        

    @staticmethod
    async def func(**kwargs):
        guild = kwargs["member"].guild
        role = discord.utils.get(guild.roles, id=roles[1])

        newPerms = role.permissions
        newPerms.update(send_messages=False)
        await role.edit(permissions=newPerms)

        asyncio.create_task(unmuteRoleAfter(role, 1800, "popushMute"))

        with open("cache.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        data["popushMute"] = getTime() + 1800
        with open("cache.json", "w", encoding="utf-8") as f:
            json.dump(data, f)


def setup(shop):
    shop.items[ShopItem.name] = ShopItem()