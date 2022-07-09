from discord.ext import commands
from achivements.achivementManager import AchivementManager
from messages import showError, showMessage
import discord

manager = AchivementManager()
desc = "Добавляет участнику достижение. Id нужного достижения можно узнать при помощи команды ы!достижения"


@commands.slash_command(name="выдать_достижение", description=desc)
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

    if achivement_id in manager.memberAchivementsIds(member):
        await ctx.respond(
            embed=showError("У участника уже есть это достижение"),
            ephemeral=True
        )
        return

    await manager.giveAchivement(member, achivement_id)
    await ctx.respond(embed=showMessage("Успешно!"))
    

def setup(bot: commands.Bot):
    bot.add_application_command(command)