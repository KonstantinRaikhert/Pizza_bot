import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == "Привет":
        await message.answer("И тебе привет")
    else:
        await message.reply(message.text)


executor.start_polling(dp, skip_updates=True)
