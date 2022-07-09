from discord.ext import commands
from database import DataBase
from config import cfg
import discord

db = DataBase()

async def getTop(sql, title, author: discord.Member, emoji):
    data = db.cur.execute(sql).fetchall()
    top = ""
    i = 1
    for memberId, messages in data:
        try:
            member = await author.guild.fetch_member(memberId)
            name = member.nick if member.nick else member.name
        except:
            name = memberId

        top += f"""{i}) **{name}**  -  __{messages}__  {emoji}\n\n"""
        i += 1
        
    return discord.Embed(
        title=title,
        description=top,
        color=cfg["color"]
    )


async def doCallback(interaction, author, sortBy, title, emoji):
    if interaction.user != author:
        return

    await interaction.message.edit(
        content=None,
        embed=await getTop(
            f"SELECT id, {sortBy} FROM users ORDER BY {sortBy} DESC LIMIT 10",
            title,
            interaction.user,
            emoji
        ),
        view=None
    )


class View(discord.ui.View):
    def __init__(self, author):
        super().__init__()
        self.author = author

    @discord.ui.button(label="Сообщения")
    async def callback1(self, button: discord.Button, interaction: discord.Interaction):
        await doCallback(interaction, self.author, "messages", "Сообщения: лидеры", "✉️")

    @discord.ui.button(label="Гейкойны")
    async def callback2(self, button, interaction: discord.Interaction):
        await doCallback(interaction, self.author, "money", "Гейкойны: лидеры", "<:gaycoin:955537976467808306>")


@commands.slash_command(name="статистика", description="Тут можно посмотреть статистику по сообщениям и деньгам")
async def command(ctx):

    await ctx.respond(
        "Какая статистика тебе нужна?",
        view=View(ctx.author)
    )

def setup(bot: commands.Bot):
    bot.add_application_command(command)