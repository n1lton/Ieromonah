from achivements.achivementManager import AchivementManager
from assets.pageManager import PageManager
from discord.ext import commands
from config import cfg
from funcy import chunks
from typing import Optional
from messages import showError
import discord

achManager = AchivementManager()

@commands.command(name="достижения")
async def command(ctx: commands.Context, member: Optional[discord.Member]):
    if ctx.message.reference:
        msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        member = msg.author

    elif member is None:
        member = ctx.author

    if member.bot:
        await ctx.reply(embed=showError("У ботов нет достижений"))
        return


    pages = []
    achs = achManager.getMemberAchivements(member, "list")

    splittedAchs = list(chunks(5, achs))

    i = 0

    for items in splittedAchs:
        i += 1
        text = ""

        for ach in items:
            text += f"**{ach[0]} {ach[2]}** - {ach[1]}\n{'Выполнено ✅' if ach[3] else 'Не выполнено ❌'} (id {ach[4]})\n\n"

        embed = discord.Embed(
            title=f"Достижения {member.nick if member.nick else member.name}",
            description=text+f"Страница {i} из {len(splittedAchs)}",
            color=cfg["color"]
        )
        pages.append(embed)

    pageManager = PageManager(pages, ctx.author)
    await pageManager.sendEmbed(ctx)




def setup(bot: commands.Bot):
    bot.add_command(command)