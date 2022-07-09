from discord.ext import commands
import discord
from database import DataBase
from assets.role import setLevel
from achivements.achivementManager import AchivementManager
from bot import Ieromonah
from discord.ext import commands
from config import otherRoles

db = DataBase()
manager = AchivementManager()

def setup(bot: commands.Bot):
    async def on_interaction(interaction: discord.Interaction):
        if interaction.custom_id is None or not interaction.custom_id.startswith("choice"):
            await commands.Bot.on_interaction(Ieromonah(), interaction)
            return

        await interaction.response.defer()
        response = interaction.custom_id.split(";")

        if response[1] == "mainrole":
            level = db.cur.execute(f"SELECT level FROM users WHERE id = {interaction.user.id}").fetchone()[0]

            if level != 0: return
                
            if response[2] == "true":
                await setLevel(interaction.user, 1) 
            else:
                await setLevel(interaction.user, 2)
                
            return

        commonRoles = set(item[0] for item in otherRoles[response[2]]) & set(role.id for role in interaction.user.roles)
        roleId = int(response[1])

        if roleId in commonRoles:
            return

        if commonRoles:
            deleteRoles = []
            for i in commonRoles:
                deleteRoles.append(discord.utils.get(interaction.user.guild.roles, id=i))

            await interaction.user.remove_roles(*deleteRoles)

        role = discord.utils.get(interaction.user.guild.roles, id=roleId)
        await interaction.user.add_roles(role)


    bot.__setattr__(on_interaction.__name__, on_interaction)