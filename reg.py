import os, discord


def reg(bot: discord.Bot):
    files = os.listdir("extentions")
    for file in files:
        if file.endswith(".py"):
            bot.load_extension(f"extentions.{file.removesuffix('.py')}")
            print(f"{file.removesuffix('.py')} command successfully loaded.")

    files = os.listdir("events")
    for file in files:
        if file.endswith(".py"):
            bot.load_extension(f"events.{file.removesuffix('.py')}")
            print(f"{file.removesuffix('.py')} event successfully loaded.")