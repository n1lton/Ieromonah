from discord.ext import commands
import discord
from database import DataBase
from random import randint
from config import roles, otherRoles

db = DataBase()

def setup(bot: commands.Bot):
    async def on_member_join(member: discord.Member):
        if member.bot:
            return
        
        data = db.cur.execute(f"SELECT level, mute FROM users WHERE id = {member.id}").fetchone()
        if data:
            level, mute = tuple(data)
            rolesToAdd = []

            rolesToAdd.append(discord.utils.get(
                member.guild.roles,
                id=roles[level]
            ))

            if mute:
                rolesToAdd.append(discord.utils.get(
                member.guild.roles,
                id=otherRoles["mute"]
            ))

            await member.add_roles(*rolesToAdd)

        else:
            db.cur.execute("INSERT INTO users (id) VALUES (?)", (member.id,))
            db.conn.commit()

        

    bot.__setattr__(on_member_join.__name__, on_member_join)