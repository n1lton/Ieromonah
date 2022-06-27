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
        
        
        db.cur.execute(f"SELECT id FROM users WHERE id = {member.id}")
        if db.cur.fetchone():
            level, mute = db.cur.execute(
                f"SELECT level, mute FROM users WHERE id = {member.id}"
            ).fetchone()[0]

            role = discord.utils.get(
                member.guild.roles,
                id=roles[level]
            )
            roles.append(discord.utils.get(
                member.guild.roles,
                id=roles[level]
            ))

            if mute:
                roles.append(discord.utils.get(
                member.guild.roles,
                id=otherRoles["mute"]
            ))

            await member.add_roles()

        

    bot.__setattr__(on_member_join.__name__, on_member_join)