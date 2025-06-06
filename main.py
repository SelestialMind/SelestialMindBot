from aiogram import Bot, Dispatcher, types
import asyncio
import os

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в SelestialMindBot!")

async def main():
    await dp.start_polling()

if name == '__main__':
    asyncio.run(main())
