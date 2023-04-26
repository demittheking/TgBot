from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
import os

TOKEN= "6118730780:AAE620cckhXKA_KsZ9Ckzg3pH5a_DvQfJv0"
bot=Bot(token= TOKEN)
dp= Dispatcher(bot)
chislo=random.randint(1,50)
fact=False

@dp.message_handler(commands=['start','help'])
async def command_start(message:types.message):
    await message.answer('Добро пожаловать в игру "Угадай число" \n Я загадал число от 1 до 50 \n Попробуй угадать, введи свой вариант числа: ')

@dp.message_handler()
async def echo_send(message: types.message):
    if int(message.text)>=1 and int(message.text)<=50 :
        if int(message.text) == chislo:
            await message.answer('Вы угадали число')
        elif int(message.text) > chislo:
            await message.answer('Не угадали, число меньше')
        else:
            await message.answer('Не угадали, число больше')
    else:
        await message.answer('Введено не число, либо число вне диапазона')

executor.start_polling(dp, skip_updates= True)