from database import DataBase
from shopAssets.baseShopItem import BaseShopItem
import discord
from config import otherRoles
from assets.mute import unmute

db = DataBase()

class ShopItem(BaseShopItem):
    name = "Размут"
    description = "Если тебя замутили, ты можешь купить размут."
    accessLevel = 2
    price = 500

    @staticmethod
    async def check(**kwargs):
        member = kwargs.get("member")
        muteRole = discord.utils.get(member.guild.roles, id=otherRoles["mute"])
        if muteRole not in member.roles:
            return "Ошибка: ты не в муте"


    @staticmethod
    async def func(**kwargs):
        member = kwargs.get("member")
        await unmute(member)


def setup(shop):
    shop.items[ShopItem.name] = ShopItem()