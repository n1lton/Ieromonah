from discord.ext import commands
from typing import Optional
from achivements.achivementManager import AchivementManager
from config import cfg
from messages import showError
from database import DataBase
import discord

manager = AchivementManager()

class View(discord.ui.View):
    completed = False

    def __init__(self, author, member, message):
        super().__init__(timeout=60)
        self.author = author
        self.member = member
        self.message=message


    async def interaction_check(self, interaction):
        if interaction.user != self.member:
            await interaction.response.defer()
            return False
        return True


    async def on_timeout(self):
        if self.completed:
            return
        embed = discord.Embed(
            title="Секс",
            description=f"{self.member.mention} проигнорил(а) пидарас сцуко 🐔",
            color=cfg["color"]
        ).set_image(url="https://cdn.discordapp.com/attachments/976915046808580139/994936476733292664/Beytman_tantsuet.gif")

        await self.message.edit(embed=embed, view=None)


    @discord.ui.button(label="Го", style=discord.ButtonStyle.green, emoji="🥵")
    async def accept(self, button: discord.Button, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Секс",
            description=f"{self.author.mention} и {self.member.mention} паебалис олдж 🤗",
            color=cfg["color"]
        ).set_image(url="https://cdn.discordapp.com/attachments/976915046808580139/994936271556313179/higurashi-rena-ryuugu.gif")

        await interaction.message.edit(embed=embed, view=None)
        
        await manager.check(self.author, 9)
        await manager.check(self.member, 9)
        self.completed = True


    @discord.ui.button(label="Нит", style=discord.ButtonStyle.red, emoji="🐔")
    async def refuse(self, button: discord.Button, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Секс",
            description=f"{self.member.mention} отказался(лась) 🐔",
            color=cfg["color"]
        ).set_image(url="https://cdn.discordapp.com/attachments/976915046808580139/994936174990868480/file.gif")

        await interaction.message.edit(embed=embed, view=None)
        self.completed = True


@commands.command(name="секс")
async def command(ctx: commands.Context, member: Optional[discord.Member]):
    if ctx.message.reference:
        msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        member = msg.author

    elif member is None:
        await ctx.reply(
            embed=discord.Embed(
                title="Секс",
                description=f"грешник {ctx.author.mention} опять рукоблудит 🐷",
                color=cfg["color"]
            ).set_image(url="https://media.discordapp.net/attachments/765783278716059672/890647894619750420/pig.gif")
        )
        return

    if member.bot:
        await ctx.reply(
            embed=showError(
                "Додикп, ты с ботом трахаца решил? Неправославно это"
            )
        )
        return

    
    embed = discord.Embed(
        title="Секс",
        description=f"{ctx.author.mention} предложил {member.mention} патрахаца 🤗",
        color=cfg["color"]
    )

    message = await ctx.reply(embed=embed)
    await message.edit(view=View(ctx.author, member, message))

    
def setup(bot: commands.Bot):
    bot.add_command(command)