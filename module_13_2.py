from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text=['Хэй!'])
async def text_message(message):
    print('Введите команду /start, чтобы начать общение.')


@dp.message_handler(text=['Urban'])
async def urban_message(message):
    print('Urban message')


@dp.message_handler(commands=['start'])
async def all_message(message):
    print('Start message')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
