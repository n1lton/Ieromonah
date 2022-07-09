from bot import Ieromonah
import discord, os
from reg import reg
from config import cfg
from database import DataBase
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = Ieromonah(cfg["prefix"], intents=intents, debug_guilds=[cfg["guild"]])



db = DataBase()
db.cur.execute(
    """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        money INTEGER DEFAULT 0,
        messages INTEGER DEFAULT 0,
        text TEXT DEFAULT "Этот текст можно изменить командой ы!описание {текст}",
        level INTEGER DEFAULT 0,
        mute INTEGER DEFAULT null,
        achivements TEXT DEFAULT ""
    )
    """
)
db.cur.execute(
    """CREATE TABLE IF NOT EXISTS stats (
        id INTEGER PRIMARY KEY,
        prayer INTEGER DEFAULT 0
    )"""
)


def main():
    reg(bot)
    load_dotenv(".env")
    bot.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()