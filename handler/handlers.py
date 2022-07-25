from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from message import message_handlers
from keyboard.keyboard import *
from bot_init import bot


async def start(message: types.Message):
    """Стартовая функция"""

    await bot.send_message(message.from_user.id, f"{message_handlers.handlers_dict['start']}",
                           reply_markup=keyboard_NewOrBU)


async def info(message: types.Message):
    """Функция справки"""

    await bot.send_message(message.from_user.id, f"{message_handlers.handlers_dict['info']}",
                           reply_markup=keyboard_Back_Menu)


async def reset(message: types.Message, state: FSMContext):
    """Данная функция предназначена для команыд сброса бота"""

    await message.answer("/start")


def register_handler_command(dp: Dispatcher):
    """Тут собраны все обработчики для функций выше"""

    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(start, Text(equals="Главное меню"))
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(reset, commands=["reset"])

