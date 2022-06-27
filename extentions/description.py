from discord.ext import commands
from messages import showError, showMessage
from database import DataBase

@commands.command(name="описание")
async def command(ctx, *, text: str):
    text = text.replace("\n", " ")

    if len(text) > 80:
        await ctx.reply(embed=showError(
            ctx,
            f"Длина текста слишком большая.\nНеобходимая длина: не больше 80 символов.\nТекущая длина: {len(text)}."
        ))
        return

    db = DataBase()
    db.cur.execute("UPDATE users SET text = ?", (text,))
    db.conn.commit()
    await  ctx.reply(embed=showMessage(ctx, f"Описание изменено успешно.\n{text}"))

def setup(bot: commands.Bot):
    bot.add_command(command)