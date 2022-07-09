from discord.ext import commands
from assets.role import setLevel
from database import DataBase
from config import cfg, otherRoles
import discord

db = DataBase()

def getEmbedAndView(title: str, cathegory: str, guild: discord.Guild):
    components = []

    for roleId, emoji in otherRoles[cathegory]:
        role = discord.utils.get(guild.roles, id=roleId)
        button = discord.ui.Button(
            label=role.name,
            emoji=emoji,
            custom_id=f"choice;{roleId};{cathegory}",
            style=discord.ButtonStyle.green
        )
        components.append(button)

    view = discord.ui.View(*components, timeout=None)
    embed = discord.Embed(
        title=title,
        color=cfg["color"]
    )
    return embed, view
        

@commands.command(name="выборроли")
async def role(ctx: commands.Context, mode: str):
    if not ctx.author.guild_permissions.administrator:
        return

    if mode == "попущ":
        embed = discord.Embed(
            title="Это самый главный вопрос, после него вам выдастся роль",
            description="**Потолок лох?**",
            color=cfg["color"]
        )
        button1 = discord.ui.Button(label="Лох", emoji="🐔", custom_id=f"choice;mainrole;true", style=discord.ButtonStyle.red)
        button2 = discord.ui.Button(label="Не лох", emoji="🤗", custom_id=f"choice;mainrole;false", style=discord.ButtonStyle.red)
        view = discord.ui.View(button1, button2, timeout=None)

    else:
        items = {
            "возраст": ("Выбор лет", "age"),
            "пол": ("Есть только 2 гендера, сосите!", "sex"),
            "ориентация": ("Педик, чи не?", "orientation"),
            "политика": ("Каковы твои политические взгляды?", "politics")
        }

        choice = items[mode]
        embed, view = getEmbedAndView(choice[0], choice[1], ctx.author.guild)

    await ctx.channel.send(embed=embed, view=view)


        

def setup(bot: commands.Bot):
    bot.add_command(role)