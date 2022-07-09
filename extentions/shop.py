from shopAssets.shopClass import Shop
from discord.ext import commands
import discord
from assets.role import setLevel




shop = Shop()


@commands.slash_command(name="магазин", description="В магазине можно купить повышение роли, размут и т.д.")
async def command(ctx):
    view = await shop.initShop(ctx)
    await ctx.respond(
        "Выбери предмет для покупки ниже 👇",
        view=view,
        ephemeral=True
    )

def setup(bot: commands.Bot):
    bot.add_application_command(command)