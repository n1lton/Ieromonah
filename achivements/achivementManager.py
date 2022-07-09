import discord, importlib, sys, os
from database import DataBase

db = DataBase()

class AchivementManager:
    achivements = {}
    # format:
    # {Achivement.id: Achivement}

    __instance = None

    def __new__(cls): # singleton pattern
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    

    def loadAchivements(self):
        for file in os.listdir("achivements\items"):
            if not file.endswith(".py"):
                continue
            name = "achivements.items."+file.removesuffix(".py")
            name = importlib.util.resolve_name(name, None)
            spec = importlib.util.find_spec(name)
            lib = importlib.util.module_from_spec(spec)
            sys.modules[name] = lib
            spec.loader.exec_module(lib)
            setup = getattr(lib, "setup")
            setup(self)

            print(f"{name.split('.')[-1]} Achivement successfully loaded.")


    async def giveAchivement(self, member, achivementId):
        await self.achivements[achivementId].getAchivement(member)


    async def check(self, member, *achivementIds, **kwargs):
        for i in achivementIds:
            await self.achivements[str(i)].check(member, **kwargs)
        
        # ебал я в рот этот ваш циркулярный импорт, если бы не он,
        # то я просто бы добавил await check(member, 5, 6, 7) в plusMoney
        if {5, 6, 7} != set(achivementIds):
            await self.check(member, 5, 6, 7)


    def getMemberAchivements(self, member: discord.Member, mode="medals"):
        achs = db.cur.execute(f"SELECT achivements FROM users WHERE id = {member.id}").fetchone()[0]

        if mode == "medals":
            tiers = [0, 0, 0]

            if achs:
                achsIds = achs.split(";")

                for achId in achsIds:
                    ach = self.achivements[achId]
                    tiers[ach.tier-1] += 1

            return f"{tiers[2]} 🥇  |  {tiers[1]} 🥈  |  {tiers[0]} 🥉"

        else:
            items = []
            for ach in self.achivements.values():
                items.append((
                    ach.name,
                    ach.description,
                    ["🥉", "🥈", "🥇"][ach.tier - 1],
                    ach.id in achs,
                    ach.id
                ))

            return items


    def addAchivement(self, achivement):
        if achivement.id in self.achivements.keys():
            raise ValueError(f"An achievement with id {achivement.id} already exists\nAchivement name: {achivement.name}")
        self.achivements[achivement.id] = achivement


    @staticmethod
    def memberAchivementsIds(member):
        achs = db.cur.execute(f"SELECT achivements FROM users WHERE id = {member.id}").fetchone()[0]
        if not achs:
            return "Отсутствуют"

        return achs.split(";")


    @staticmethod
    def takeAchivement(member, achivementId):
        achs = db.cur.execute(f"SELECT achivements FROM users WHERE id = {member.id}").fetchone()[0].split(";")
        achs.remove(achivementId)
        db.cur.execute(f"UPDATE users SET achivements = '{';'.join(achs)}'")
        db.conn.commit()