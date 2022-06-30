from discord.ext import commands
from config import cfg
import discord

@commands.command(name="донат")
async def command(ctx):
    desc = """**По донату писать <@569497732889182208>**
Этим вы сильно поможете в разработке бота, а также получите гейкойны <:gaycoin:955537976467808306>

1 Рубль = 10 <:gaycoin:955537976467808306>.
При донате от 200 Рублей бонус 50%. Т.е. вы закинули 200 Руб. и получили 3000 <:gaycoin:955537976467808306>.

P.S. Коля легенда"""
    embed = discord.Embed(
        title="Донат",
        description=desc,
        color=cfg["color"]
    )
    await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_command(command)