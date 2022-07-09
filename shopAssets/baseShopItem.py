import discord
from database import DataBase
from config import cfg, roles
from assets.moneyFunc import plusMoney

db = DataBase()

class BaseShopItem:
    name = None
    description=None
    accessLevel = 0
    price = None


    @staticmethod
    async def func(**kwargs):
        pass


    @staticmethod
    async def check(**kwargs):
        return None


    async def getPrice(self, **kwargs):
        return self.price


    async def sendEmbed(self, interaction:discord.Interaction, **kwargs):
        self.price = await self.getPrice(**kwargs)
        member = kwargs.get("member")

        embed = discord.Embed(
            title=self.name,
            description=self.description,
            color=cfg["color"]
        ).add_field(
            name="Цена",
            value=self.price
        ).add_field(
            name="Необходимая роль",
            value="Любая" if self.accessLevel < 2 else discord.utils.get(
                member.guild.roles, id=roles[self.accessLevel]
            ).name
        )

        class View(discord.ui.View):
            item = self

            @discord.ui.button(label="Купить", style=discord.ButtonStyle.primary)
            async def button_callback(self, button, interaction):
                buyEmbed = await self.item.buy(**kwargs)

                await interaction.response.send_message(
                    embed=buyEmbed,
                    ephemeral=True
                )

        await interaction.response.send_message(
            content=None,
            embed=embed,
            view=View(),
            ephemeral=True
        )


    async def buy(self, **kwargs):
        member = kwargs.get("member")
        db.cur.execute(f"SELECT level, money FROM users WHERE id = {member.id}")
        level, money = db.cur.fetchone()

        checkResult = await self.check(**kwargs)

        if checkResult:
            desc = checkResult

        elif level < self.accessLevel:
            desc = "Ошибка: неподходящая роль"

        elif money < self.price:
            desc = "Ошибка: недостаточно средств"

        else:
            await plusMoney(member, -self.price)
            await self.func(**kwargs)
            desc = "Успешно"


        return discord.Embed(
            title="Покупка",
            description=desc,
            color=cfg["color"]
        )