from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboard.keyboard_bu_inline import *
from aiogram import types, Dispatcher
from message.message_handlers import *
from keyboard.keyboard_bu import *
from keyboard.keyboard import *
from state.states import *
from bot_init import bot


async def start_bu(message: types.Message, state: FSMContext):
    """ Тут указываем по какому количеству параметров будет производиться поиск """

    await state.update_data(
        {"chose_param": None,
         "region": None,
         "category": None,
         "body": None,
         "marka": None,
         "model": None,
         "year": None,
         "price": None,
         "fuel": None,
         "KPP": None,
         "volume": None
         })

    await bot.send_message(message.from_user.id, f"{handlers_bu_dict['start_bu']}",
                           reply_markup=keyboard_start_bu())


async def manual_param(message: types.Message):
    """ Тут проверяем, что пользователь ввел, для след направления машины состояния """

    await bot.send_message(message.from_user.id, f"{handlers_bu_dict['manual_param']}",
                           reply_markup=keyboard_choose())
    await bot.send_message(message.from_user.id, f"{handlers_bu_dict['manual_param_2']}",
                           reply_markup=keyboard_Accept_Param())


async def region(message: types.Message, state: FSMContext):
    """ Тут указываем в каких регионах будем искать обьявления """

    answer = message.text
    print(f"{answer} region")

    if answer.isdigit():
        # Эта проверка для целых чисел, и последовательной работы машины

        await state.update_data(
            {"chose_param": int(answer)})

        await bot.send_message(message.from_user.id, f"def region {handlers_bu_dict['region']}",
                               reply_markup=keyboard_region())

        data = await state.get_data()
        check_param = data.get("chose_param")

        if check_param == 1:
            await QuestionParams.question_ended.set()
        elif check_param > 1:
            await QuestionParams.question_category.set()

    elif answer == "Продолжить ->":
        # Эта проверка для списка который указал пользователь, и НЕ последовательной работы машины

        actual_dict_param = []
        for i in keyboard_choose()["inline_keyboard"]:
            for j in i:
                if j["text"][-1].startswith('✅'):
                    actual_dict_param.append(j["text"][-3])
        await bot.send_message(message.from_user.id, f"{actual_dict_param}")

        await state.update_data(
            {"chose_param": actual_dict_param})

        await bot.send_message(message.from_user.id, "Выбран рандомный вариант, он еще в разработке",
                               reply_markup=keyboard_Test)

        await state.finish()


async def category(message: types.Message, state: FSMContext):
    """Тут указываем в какой категории будем производить поиск"""

    answer = message.text
    print(f"{answer} category")

    if answer == "Назад":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_bu_dict['start_bu']}"
                               , reply_markup=keyboard_start_bu)

    elif answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()
        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"region": answer})

            await bot.send_message(message.from_user.id, f"def category {handlers_bu_dict['category']}",
                                   reply_markup=keyboard_category())

            if check_param == 2:
                await QuestionParams.question_ended.set()
            elif check_param > 2:
                await QuestionParams.question_body.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"region": answer})

            await bot.send_message(message.from_user.id, f"{handlers_bu_dict['category']}",
                                   reply_markup=keyboard_category())
            await state.finish()


async def body(message: types.Message, state: FSMContext):
    """ Тут указываем тип кузова который будем искать в обьявлениях """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()
        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"category": answer})

            await bot.send_message(message.from_user.id, f"def body {handlers_bu_dict['body']} {answer}\n\n"
                                                         f"{handlers_bu_dict['body_2']}",
                                   reply_markup=keyboard_body(answer))

            if check_param == 3:
                await QuestionParams.question_ended.set()
            elif check_param > 3:
                await QuestionParams.question_marka.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"category": answer})

            await bot.send_message(message.from_user.id, f"{handlers_bu_dict['body']} {answer}\n\n"
                                                         f"{handlers_bu_dict['body_2']}",
                                   reply_markup=keyboard_body(answer))
            await state.finish()


async def marka(message: types.Message, state: FSMContext):
    """ Тут указываем марку которую будем искать в обьявлениях """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()
        check_param = data.get("chose_param")
        category = data.get("category")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"body": answer})


            await bot.send_message(message.from_user.id, f"def marka {handlers_bu_dict['marka']} {answer} "
                                                         f"{handlers_bu_dict['marka_2']}",
                                   reply_markup=keyboard_marka(category))

            if check_param == 4:
                await QuestionParams.question_ended.set()
            elif check_param > 4:
                await QuestionParams.question_model.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"body": answer})

            await bot.send_message(message.from_user.id, f"{handlers_bu_dict['marka']} {answer} "
                                                         f"{handlers_bu_dict['marka_2']}",
                                   reply_markup=keyboard_marka(category))
            await state.finish()


async def model(message: types.Message, state: FSMContext):
    """ Тут указываем модель которую будем искать в обьявлениях """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()

        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"marka": answer})

            category = data.get("category")
            await bot.send_message(message.from_user.id, f"def model {handlers_bu_dict['model']} {answer} "
                                                         f"{handlers_bu_dict['model_2']}",
                                   reply_markup=keyboard_model(category, answer))

            if check_param == 5:
                await QuestionParams.question_ended.set()
            elif check_param > 5:
                await QuestionParams.question_year.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"marka": answer})

            category = data.get("category")
            await bot.send_message(message.from_user.id, f"{handlers_bu_dict['model']} {answer} "
                                                         f"{handlers_bu_dict['model_2']}",
                                   reply_markup=keyboard_model(category, answer))
            await state.finish()


async def year(message: types.Message, state: FSMContext):
    """ Тут указываем год от которого и до которого будем искать в обьявлениях """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()

        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"model": answer})

            await bot.send_message(message.from_user.id, f"def from year {handlers_bu_dict['from_year']} {answer} "
                                                         f"{handlers_bu_dict['from_year_2']}",
                                   reply_markup=keyboard_year_price())

            if check_param == 6:
                await QuestionParams.question_ended.set()
            elif check_param > 6:
                await QuestionParams.question_price.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"model": answer})

            await bot.send_message(message.from_user.id, f"def year {handlers_bu_dict['from_year']} {answer} "
                                                         f"{handlers_bu_dict['from_year_2']}",
                                   reply_markup=keyboard_year_price())
            await state.finish()


async def price(message: types.Message, state: FSMContext):
    """ Тут указываем цену от и до которой будем искать в обьявления """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()

        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"year": answer})

            await bot.send_message(message.from_user.id, f"def price {handlers_bu_dict['from_price']} {answer} "
                                                         f"{handlers_bu_dict['from_price_2']}",
                                   reply_markup=keyboard_year_price())

            if check_param == 7:
                await QuestionParams.question_ended.set()
            elif check_param > 7:
                await QuestionParams.question_fuel.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"year": answer})

            await bot.send_message(message.from_user.id, f"def from year {handlers_bu_dict['from_price']} {answer} "
                                                         f"{handlers_bu_dict['from_price_2']}",
                                   reply_markup=keyboard_year_price())
            await state.finish()


async def fuel(message: types.Message, state: FSMContext):
    """ Тут указываем тип топлива которой будем искать в обьявления """

    answer = message.text

    data = await state.get_data()
    category = data.get("category")

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    elif category == "Прицепы":
        await bot.send_message(message.from_user.id, f"У категории {category} нету остальных параметров",
                               reply_markup=keyboard_continiue)
        await QuestionParams.question_ended.set()

    else:
        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"price": answer})

            await bot.send_message(message.from_user.id, f"def fuel {handlers_bu_dict['fuel']} {answer} "
                                                         f"{handlers_bu_dict['fuel_2']}",
                                   reply_markup=keyboard_fuel())

            if check_param == 8:
                await QuestionParams.question_ended.set()
            elif check_param > 8:
                await QuestionParams.question_kpp.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"year": answer})

            await bot.send_message(message.from_user.id, f"def from year {handlers_bu_dict['fuel']} {answer} "
                                                         f"{handlers_bu_dict['fuel_2']}",
                                   reply_markup=keyboard_fuel())
            await state.finish()


async def kpp(message: types.Message, state: FSMContext):
    """ Тут указываем тип коробки передач которую будем искать в обьявления """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()

        check_param = data.get("chose_param")

        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"fuel": answer})

            await bot.send_message(message.from_user.id, f"def kpp {handlers_bu_dict['kpp']} {answer} "
                                                         f"{handlers_bu_dict['kpp_2']}",
                                   reply_markup=keyboard_kpp())

            if check_param == 9:
                await QuestionParams.question_ended.set()
            elif check_param > 9:
                await QuestionParams.question_volume.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"year": answer})

            await bot.send_message(message.from_user.id, f"def kpp {handlers_bu_dict['kpp']} {answer} "
                                                         f"{handlers_bu_dict['kpp_2']}",
                                   reply_markup=keyboard_kpp())
            await state.finish()


async def volume(message: types.Message, state: FSMContext):
    """ Тут указываем тип топлива которой будем искать в обьявления """

    answer = message.text

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    else:
        data = await state.get_data()

        check_param = data.get("chose_param")
        category = data.get("category")


        if isinstance(check_param, int):
            # Тут происходит проверка на последовательный ввод и последовательное выполнение машины

            await state.update_data(
                {"kpp": answer})

            await bot.send_message(message.from_user.id, f"def volume {handlers_bu_dict['volume']} {answer} "
                                                         f"{handlers_bu_dict['volume_2']}",
                                   reply_markup=keyboard_volume(category))

            if check_param == 10:
                await QuestionParams.question_ended.set()

        elif isinstance(check_param, list):
            # Тут происходит проверка на НЕ последовательный ввод и рандомного выполнение машины
            await state.update_data(
                {"year": answer})

            await bot.send_message(message.from_user.id, f"def volume {handlers_bu_dict['volume']} {answer} "
                                                         f"{handlers_bu_dict['volume_2']}",
                                   reply_markup=keyboard_volume(category))
            await state.finish()


async def ended(message: types.Message, state: FSMContext):
    """ Тут мы обрабатываем запрос пользователя """

    answer = message.text

    data = await state.get_data()
    check_param = data.get("chose_param")

    if answer == "Главное меню":
        await state.finish()
        await bot.send_message(message.from_user.id, f"{handlers_dict['start']}",
                               reply_markup=keyboard_NewOrBU)

    list_param = {"1": "region",
                  "2": "category",
                  "3": "body",
                  "4": "marka",
                  "5": "model",
                  "6": "year",
                  "7": "price",
                  "8": "fuel",
                  "9": "kpp",
                  "10": "volume"
                  }

    for i in list_param:
        if check_param == int(i):
            await state.update_data(
                {f"{list_param[f'{check_param}']}": answer})
            data_2 = await state.get_data()

            await bot.send_message(message.from_user.id, f"{handlers_bu_dict[f'ended_{check_param}']}\n{data_2}",
                                   reply_markup=types.ReplyKeyboardRemove())

            await state.finish()


async def reset(message: types.Message, state: FSMContext):
    """Данная функция предназначена для команыд сброса бота"""

    await state.finish()
    await message.answer("/start")


def register_handler_command_bu(dp: Dispatcher):
    """Тут собраны все обработчики для функций выше"""

    dp.register_message_handler(start_bu, Text(equals="Б/У"))
    dp.register_message_handler(manual_param, Text(equals="Ввести параметры вручную"))
    dp.register_message_handler(region, Text(equals="Продолжить ->"))
    dp.register_message_handler(start_bu, Text(equals="Назад"))

    dp.register_message_handler(region, Text(equals="1"))
    dp.register_message_handler(region, Text(equals="2"))
    dp.register_message_handler(region, Text(equals="3"))
    dp.register_message_handler(region, Text(equals="4"))
    dp.register_message_handler(region, Text(equals="5"))
    dp.register_message_handler(region, Text(equals="6"))
    dp.register_message_handler(region, Text(equals="7"))
    dp.register_message_handler(region, Text(equals="8"))
    dp.register_message_handler(region, Text(equals="9"))
    dp.register_message_handler(region, Text(equals="10"))


    dp.register_message_handler(start_bu, state=QuestionParams.start_bu)

    dp.register_message_handler(region, state=QuestionParams.question_region)
    dp.register_message_handler(category, state=QuestionParams.question_category)
    dp.register_message_handler(body, state=QuestionParams.question_body)
    dp.register_message_handler(marka, state=QuestionParams.question_marka)
    dp.register_message_handler(model, state=QuestionParams.question_model)
    dp.register_message_handler(year, state=QuestionParams.question_year)
    dp.register_message_handler(price, state=QuestionParams.question_price)
    dp.register_message_handler(fuel, state=QuestionParams.question_fuel)
    dp.register_message_handler(kpp, state=QuestionParams.question_kpp)
    dp.register_message_handler(volume, state=QuestionParams.question_volume)

    dp.register_message_handler(ended, state=QuestionParams.question_ended)
