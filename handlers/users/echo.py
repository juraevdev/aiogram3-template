from aiogram import Router, types


echo_router = Router()
# Echo bot
@echo_router.message()
async def bot_echo(message: types.Message):
    await message.answer(message.text)
