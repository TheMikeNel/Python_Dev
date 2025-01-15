import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

baseLog = logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
API_TOKEN = '7359851076:AAE-Eg4uyLWi3ST_Ceu492fGQ8Qz0RJZMNg'

dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.reply("Привет!\nЯ Эхо-бот от Zero!\nОтправьвь мне любое сообщение, а я тебе обязательно отвечу (а может и нет).")
    logging.info("Welcome sended")

@dp.message(Command('okurwa'))
async def send_welcome(message: Message) -> None:
    await message.reply("Kurrwa BOBER Ja pierdole!\U0001F440")
    logging.info("Kurrwa bobra sended!")

@dp.message()
async def echo(message: Message) -> None:
    await message.answer("Echo..." + message.text)

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())