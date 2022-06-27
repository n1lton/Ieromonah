from discord.ext import commands
from extentions.mute import unmute
from config import cfg, otherRoles
from messages import showError
import discord

@commands.has_guild_permissions(mute_members=True)
@commands.slash_command(name="размут", description="Размучивает челика")
async def command(ctx, member: discord.Member):
    if not ctx.author.guild_permissions.mute_members:
        await ctx.respond(
            embed=showError("Нет прав"),
            ephemeral=True
    )


    role = discord.utils.get(member.guild.roles, id=otherRoles["mute"])

    if role not in member.roles:
        await ctx.respond(embed=showError("Участник не в муте"))
        return

    await unmute(member)
    await ctx.respond(
        embed=discord.Embed(
            title="Мут",
            description=f"{ctx.author.mention} размутил {member.mention}",
            color=cfg["color"]
        )
    )

def setup(bot: commands.Bot):
    bot.add_application_command(command)