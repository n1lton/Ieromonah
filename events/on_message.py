from discord.ext import commands
import discord
from database import DataBase
from random import randint
from config import spamChannels

db = DataBase()

def setup(bot: commands.Bot):
    async def on_message(message: discord.Message):
        await bot.process_commands(message)

        if message.author.bot or message.channel.id in spamChannels:
            return
        
        db.cur.execute(f"SELECT id FROM users WHERE id = {message.author.id}")
        if db.cur.fetchone():
            db.cur.execute(
                "UPDATE users SET money = money + ?, messages = messages + 1 WHERE id = ?",
                (randint(0, 1), message.author.id)
            )
            db.conn.commit()

        

    bot.__setattr__(on_message.__name__, on_message)