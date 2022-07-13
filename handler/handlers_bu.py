from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from state.states import *
from keyboard.keyboard_bu import *
from bot_init import bot


async def start_bu(message: types.Message):
    """Тут указываем по какому количеству параметров будет производиться поиск"""

    await bot.send_message(message.from_user.id, "Какой тип поиска Вы хотите использовать:\n\n"
                                                 "2 параметра:\nТип транспорта\n Марка\n\n"
                                                 "5 параметров:\nТип транспорта\n"
                                                 "Марка\nМодель\n"
                                                 "Год От/До\nЦена От/До",
                           reply_markup=keyboard_Params)
    await QuestionParams.question_category.set()


async def category(message: types.Message, state: FSMContext):
    answer = message.text
    print(answer)
    if answer == "2 параметра":
        await state.update_data(
            {"chose_param": 2})
    elif answer == "5 параметров":
        await state.update_data(
            {"chose_param": 5})

    await bot.send_message(message.from_user.id, "Виберите одну из категорий в которой хотите произвести поиск",
                           reply_markup=keyboard_category)
    await QuestionParams.question_marka.set()


async def marka(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"category": answer})
    if answer == "Легковые":
        await bot.send_message(message.from_user.id, f"Вы выбрали категорию {answer}\n\n"
                                                     f"Какую марку Вы хотите использовать в поиске ?\n"
                                                     "Выберите из предоставленных ниже вариантом, или введите вручную",
                               reply_markup=keyboard_topMarks_Lehkovie)
        await QuestionParams.question_model.set()

    elif answer == "Мото":
        await bot.send_message(message.from_user.id, f"Вы выбрали категорию {answer}\n\n"
                                                     f"Какую марку Вы хотите использовать в поиске ?\n"
                                                     "Выберите из предоставленных ниже вариантом, или введите вручную",
                               reply_markup=keyboard_topMarks_Moto)
        await QuestionParams.question_model.set()

    elif answer == "Водный транспорт":
        await bot.send_message(message.from_user.id, f"Вы выбрали категорию {answer}\n\n"
                                                     f"Какую марку Вы хотите использовать в поиске ?\n"
                                                     "Выберите из предоставленных ниже вариантом, или введите вручную",
                               reply_markup=keyboard_topMarks_VodniyTransport)
        await QuestionParams.question_model.set()


async def model(message: types.Message, state: FSMContext):
    answer = message.text
    print(answer)
    await state.update_data(
        {"marka": answer})

    if answer == "Назад":
        # await state.finish()
        await bot.send_message(message.from_user.id, "Выберите категорию еще раз", reply_markup=keyboard_category)
        await QuestionParams.question_marka.set()
    else:

        data = await state.get_data()
        check_param = data.get("chose_param")
        print(type(check_param))
        if check_param == 2:
            print("Finish")
            print(data)
            await bot.send_message(message.from_user.id, "Ваш запрос выполняется, ожидайте...")
            await state.finish()
        elif check_param == 5:
            answer = message.text
            await state.update_data(
                {"marka": answer})

            data = await state.get_data()
            category_ = data.get("marka")

            await bot.send_message(message.from_user.id, f"Какую модель марки {category_} Вы хотите найти ?")

            await QuestionParams.question_from_year.set()


async def from_year(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"model": answer})
    await bot.send_message(message.from_user.id, "Укажите в формате: '1998' с какого года рассматриваем варианты")

    await QuestionParams.question_to_year.set()


async def to_year(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"from_year": answer})
    await bot.send_message(message.from_user.id, "Укажите в формате: '2014' до какого года рассматриваем варианты")

    await QuestionParams.question_from_price.set()


async def from_price(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"to_year": answer})
    await bot.send_message(message.from_user.id, "Укажите в формате: '50000' сумму от которой рассматривать варианты")

    await QuestionParams.question_to_price.set()


async def to_price(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"from_price": answer})
    await bot.send_message(message.from_user.id, "Укажите в формате: '250000' сумму до которой рассматривать варианты")

    await QuestionParams.question_ended.set()


async def ended(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"to_price": answer})
    await bot.send_message(message.from_user.id, "Ваш запрос выполняется, ожидайте...")
    data = await state.get_data()
    print("Finish")
    print(data)
    await state.finish()


async def reset(message: types.Message, state: FSMContext):
    """Данная функция предназначена для команыд сброса бота"""

    await state.finish()
    await message.answer("/start")


def register_handler_command(dp: Dispatcher):
    """Тут собраны все обработчики для функций выше"""

    dp.register_message_handler(start_bu, Text(equals="Б/У"))

    dp.register_message_handler(category, state=QuestionParams.question_category)
    dp.register_message_handler(marka, state=QuestionParams.question_marka)
    dp.register_message_handler(model, state=QuestionParams.question_model)
    dp.register_message_handler(from_year, state=QuestionParams.question_from_year)
    dp.register_message_handler(to_year, state=QuestionParams.question_to_year)
    dp.register_message_handler(from_price, state=QuestionParams.question_from_price)
    dp.register_message_handler(to_price, state=QuestionParams.question_to_price)
    dp.register_message_handler(ended, state=QuestionParams.question_ended)
