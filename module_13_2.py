from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7238999474:AAHSB6E1wOVoJnw_l2FzlUtATnAcWDtpcQA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def all_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text=['Хэй!'])
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


@dp.message_handler(text=['Urban'])
async def all_message(message):
    print('Urban message')


@dp.message_handler(commands=['start'])
async def all_message(message):
    print('Start message')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
