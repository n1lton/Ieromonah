import os, discord
from achivements.achivementManager import AchivementManager
from shopAssets.shopClass import Shop

manager = AchivementManager()
shop = Shop()


def reg(bot: discord.Bot):
    print("Commands registration...\n")
    files = os.listdir("extentions")
    for file in files:
        if file.endswith(".py"):
            bot.load_extension(f"extentions.{file.removesuffix('.py')}")
            print(f"{file.removesuffix('.py')} command successfully loaded.")

    print("\n\nEvents registration...\n")
    files = os.listdir("events")
    for file in files:
        if file.endswith(".py"):
            bot.load_extension(f"events.{file.removesuffix('.py')}")
            print(f"{file.removesuffix('.py')} event successfully loaded.")

    print("\n\nAchivements registration...\n")
    manager.loadAchivements()

    print("\n\nShopItems registration...\n")
    shop.loadItems()