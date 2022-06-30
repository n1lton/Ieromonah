from database import DataBase
from shopAssets.baseShopItem import BaseShopItem
import discord, json, asyncio
from config import otherRoles
from assets.mute import unmuteRoleAfter
from time import time as getTime
from config import roles

db = DataBase()

class ShopItem(BaseShopItem):
    name = "Мут всех на 30 минут"
    description = "Изменяет разрешения всех ролей, запрещая писать сообщения"
    accessLevel = 3
    price = 2500

    @staticmethod
    async def check(**kwargs):
        with open("cache.json", "r", encoding="utf-8") as f:
            if json.load(f)["allMute"]:
                return "Ошибка: кто-то уже замутил всех"
        

    @staticmethod
    async def func(**kwargs):
        guild = kwargs["member"].guild
        for roleId in roles[1:]: # без агностика
            role = discord.utils.get(guild.roles, id=roleId)

            newPerms = role.permissions
            newPerms.update(send_messages=False)
            await role.edit(permissions=newPerms)

            asyncio.create_task(unmuteRoleAfter(role, 1800, "allMute"))


        with open("cache.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        data["allMute"] = getTime() + 1800
        with open("cache.json", "w", encoding="utf-8") as f:
            json.dump(data, f)


def setup(shop):
    shop.items[ShopItem.name] = ShopItem()