from aiogram import Router, types
from aiogram.filters import Command

help_router = Router()

@help_router.message(Command("help"))
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
