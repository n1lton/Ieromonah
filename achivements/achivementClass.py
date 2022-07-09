from bot import Ieromonah
import discord
from database import DataBase
from config import cfg, otherChannels

db = DataBase()
bot = Ieromonah()

class Achivement:
    def __init__(self, name, tier, description, id):
        self.name = name
        
        # tiers: 1 - bronze, 2 - silver, 3 - gold
        if not (0 < tier < 4):
            raise ValueError("tier must be > 0 and < 4")

        self.tier = tier
        self.description = description
        self.id = str(id)

    
    def __str__(self):
        return f"Achivement Object '{self.name} - {self.description}'"


    def setCheck(self, func):
        async def check(member, **kwargs):
            achs = db.cur.execute(f"SELECT achivements FROM users WHERE id = {member.id}").fetchone()[0]
            if self.id in achs.split(";"):
                return

            result = await func(member, **kwargs)
            if result:
                await self.getAchivement(member)

        self.check = check


    async def getAchivement(self, member):
        reward = 10 ** self.tier
        achivLevel = ["🥉", "🥈", "🥇"][self.tier - 1]

        # write to db
        achs = db.cur.execute(f"SELECT achivements FROM users WHERE id = {member.id}").fetchone()[0]
        
        if achs:
            newAchs = achs + ";" + self.id

        else:
            newAchs = self.id

        db.cur.execute(f"UPDATE users SET achivements = '{newAchs}', money = money + {reward} WHERE id = {member.id}")
        db.conn.commit()

        # sending message
        embed = discord.Embed(
            title=f"Достижение разблокировано!  {achivLevel}",
            description=f"{member.mention} получил достижение: __{self.name}__",
            color=cfg["color"]
        ).add_field(
            name="Описание",
            value=self.description,
            inline=False
        ).add_field(
            name="Награда",
            value=f"{reward} <:gaycoin:955537976467808306>",
            inline=True
        )

        channel = await bot.fetch_channel(otherChannels["spam"])
        await channel.send(embed=embed)

        