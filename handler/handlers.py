from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from keyboard.keyboard import *
from bot_init import bot


async def start(message: types.Message):
    """Стартовая функция"""

    await bot.send_message(message.from_user.id, "Тут будет обьясняться логика перемещения по боту и перечень всех"
                                                 " команд которыми пользователь сможет пользоваться",
                           reply_markup=keyboard_start)


async def chose_new_bu(message: types.Message):
    """Функция которая будет напрвялть пользователя в машину состояния Б/У или Новые"""

    await bot.send_message(message.from_user.id, "Виберите в каком разделе Вы хотите произвести поиск,"
                                                 " Новые или Б/У автомобили ?\n\n\nПри нажатии на НОВЫЕ"
                                                 "Мы получим пример запроса со всеми марками",
                           reply_markup=keyboard_NewOrBU)


async def info(message: types.Message):
    """Функция справки"""

    await bot.send_message(message.from_user.id, "Тут можно подробно расписать, как пользоваться ботом и рассписать"
                                                 "как бот будет искать предложения по сайту",
                           reply_markup=keyboard_button_continued)


async def reset(message: types.Message, state: FSMContext):
    """Данная функция предназначена для команыд сброса бота"""

    await state.finish()
    await message.answer("/start")


def register_handler_command(dp: Dispatcher):
    """Тут собраны все обработчики для функций выше"""

    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(reset, commands=["reset"])
    dp.register_message_handler(info, commands=["info"])

    dp.register_message_handler(chose_new_bu, Text(equals="Все понятно, можно начинать"))
    dp.register_message_handler(info, Text(equals="Детальное описание работы с ботом"))
    dp.register_message_handler(chose_new_bu, Text(equals="Продолжить"))

    # dp.register_message_handler(start_new, Text(equals="Новые"))
    # dp.register_message_handler(chose_param, Text(equals="Б/У"))
    #
    # dp.register_message_handler(category, state=QuestionParams.question_category)
    # dp.register_message_handler(marka, state=QuestionParams.question_marka)
    # dp.register_message_handler(model, state=QuestionParams.question_model)
    # dp.register_message_handler(from_year, state=QuestionParams.question_from_year)
    # dp.register_message_handler(to_year, state=QuestionParams.question_to_year)
    # dp.register_message_handler(from_price, state=QuestionParams.question_from_price)
    # dp.register_message_handler(to_price, state=QuestionParams.question_to_price)
    # dp.register_message_handler(ended, state=QuestionParams.question_ended)
