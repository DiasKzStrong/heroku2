from aiogram import types
from loader import dp

@dp.message_handler(content_types=['text'])
async def command_start(message: types.Message):
    await message.delete()

