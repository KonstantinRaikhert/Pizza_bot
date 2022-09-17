import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот вышел в онлайн")


@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита")
        await message.delete()
    except:
        url = os.getenv("BOT_URL")
        await message.reply(f"Общение с ботом через ЛС, напишите ему:\n{url}")


@dp.message_handler(commands=["Режим_работы"])
async def pizza_open_command(message: types.Message):
    await bot.send_message(
        message.from_user.id, "Вс-Чт с 9:00 до 20:00б Пт-Сб с 10:00 до 23:00"
    )


@dp.message_handler(commands=["Расположение"])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ул. Колбасная 15")


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == "Привет":
        await message.answer("И тебе привет")
    else:
        await message.reply(message.text)


executor.start_polling(dp, skip_updates=True)
