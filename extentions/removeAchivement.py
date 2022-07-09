from discord.ext import commands
from achivements.achivementManager import AchivementManager
from messages import showError, showMessage
import discord

manager = AchivementManager()
desc = "Забирать у участника достижение. Id нужного достижения можно узнать при помощи команды ы!достижения"


@commands.slash_command(name="забрать_достижение", description=desc)
async def command(ctx, member: discord.Member, achivement_id: str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.respond(
            embed=showError("Нет прав"),
            ephemeral=True
        )
        return

    if member.bot:
        await ctx.respond(
            embed=showError("У ботов нет достижений"),
            ephemeral=True
        )
        return


    if achivement_id not in manager.achivements:
        await ctx.respond(
            embed=showError("Достижения с таким id не существует"),
            ephemeral=True
        )
        return

    if achivement_id not in manager.memberAchivementsIds(member):
        await ctx.respond(
            embed=showError("У участника нет этого достижения"),
            ephemeral=True
        )
        return

    manager.takeAchivement(member, achivement_id)
    await ctx.respond(embed=showMessage("Успешно!"))
    

def setup(bot: commands.Bot):
    bot.add_application_command(command)