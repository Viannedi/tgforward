from aiogram import Bot, types
from aiogram.utils import executor
from aiogram import types
from aiogram.dispatcher import Dispatcher

token = '1'
bot = Bot(token=token)
dp = Dispatcher(bot)
admin_id = 0


@dp.message_handler(commands=['start'])
async def process_voice_command(message: types.Message):
    await message.reply('Привет напишите любое сообщение и оно будет доставлено администратору')


@dp.message_handler()
async def forward_admin(message: types.Message):
    await message.forward(admin_id)


if __name__ == '__main__':
    executor.start_polling(dp)
