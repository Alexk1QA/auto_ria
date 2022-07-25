import requests
from dotenv import load_dotenv
import os

load_dotenv()


def test_category():
    """ Временная функция !!! Возвращает ТИПЫ ТРАНСПОРТА

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    reqsts_category = requests.get(f"https://developers.ria.com/auto/categories/?api_key={os.getenv('API_KEY')}").json()

    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_category:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 1000:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all


# pprint(test_category()[1])


def test_region():
    """ Временная функция !!! Возвращает РЕГИОНЫ

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    reqsts_region = requests.get(f"https://developers.ria.com/auto/states?api_key={os.getenv('API_KEY')}").json()


    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_region:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 500:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all


# pprint(test_region()[1])


def test_body(value_categories):
    """ Временная функция !!! Возвращает ТИПЫ КУЗОВА

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    global value_categories_param

    dict_category = {
        "Легковые":"1",
        "Мото": "2",
        "Водный транспорт": "3",
        "Спецтехника": "4",
        "Прицепы": "5",
        "Грузовики": "6",
        "Автобусы": "7",
        "Автодома": "8",
        "Воздушный транспорт": "9",
        "Сельхозтехника": "10"
    }

    if dict_category.get(value_categories):
        value_categories_param = dict_category[f"{value_categories}"]

    reqsts_bodystyles = requests.get(f"https://developers.ria.com/auto/categories/{value_categories_param}/bodystyles?"
                                     f"api_key={os.getenv('API_KEY')}").json()

    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_bodystyles:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 1000:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all


# pprint(test_body("Легковые")[1])


def test_marka(value_categories):
    """ Временная функция !!! Возвращает МАРКИ

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    global value_categories_param

    dict_category = {
        "Легковые": "1",
        "Мото": "2",
        "Водный транспорт": "3",
        "Спецтехника": "4",
        "Прицепы": "5",
        "Грузовики": "6",
        "Автобусы": "7",
        "Автодома": "8",
        "Воздушный транспорт": "9",
        "Сельхозтехника": "10"
    }

    if dict_category.get(value_categories):
        value_categories_param = dict_category[f"{value_categories}"]

    reqsts_marks = requests.get(f"https://developers.ria.com/auto/categories/{value_categories_param}/"
                                     f"marks?api_key={os.getenv('API_KEY')}").json()

    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_marks:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 1000:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all


# pprint(test_marka("Легковые")[1])


def test_model(value_categories, marka):
    """ Временная функция !!! Возвращает МОДЕЛИ

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    global value_categories_param, reqsts_models

    dict_category = {
        "Легковые": "1",
        "Мото": "2",
        "Водный транспорт": "3",
        "Спецтехника": "4",
        "Прицепы": "5",
        "Грузовики": "6",
        "Автобусы": "7",
        "Автодома": "8",
        "Воздушный транспорт": "9",
        "Сельхозтехника": "10"
    }
    print(value_categories, marka)

    if dict_category.get(value_categories):
        value_categories_param = dict_category[f"{value_categories}"]


        reqsts_marks = requests.get(f"https://developers.ria.com/auto/categories/{value_categories_param}/"
                                     f"marks?api_key={os.getenv('API_KEY')}").json()

        for i in reqsts_marks:
            name_categories = i["name"]
            value_categories = i["value"]
            if name_categories == marka:
                reqsts_models = requests.get(f"http://api.auto.ria.com/categories/{value_categories_param}/"
                                            f"marks/{value_categories}/models?"
                                            f"api_key={os.getenv('API_KEY')}").json()

    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_models:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 1000:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all

# marka = "Kraemer"
# pprint(test_model("Прицепы", marka))


def test_fuel():
    """ Временная функция !!! Возвращает ТИП ТОПЛИВА

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    reqsts_fuel = requests.get(f"https://developers.ria.com/auto/type?api_key={os.getenv('API_KEY')}").json()

    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_fuel:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 1000:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all


# pprint(test_fuel()[1])


def test_kpp():
    """ Временная функция !!! Возвращает ТИПЫ КОРОБОК ПЕРЕДАЧ

        Переводит запрос в читабельный вид для отправки в чат.

        test_body(1)[0]) - первый параметр тип транспорта, второй указывается для типа возращаемых данных
        0 - Вернет сообщение переменную для отправки в норм виде в чат
        1 - веррнет словарь для работы с функцией
    """

    reqsts_kpp = requests.get(f"https://developers.ria.com/auto/categories/2/"
                               f"gearboxes?api_key={os.getenv('API_KEY')}").json()

    dict_category = {}
    message = ""
    list_all = []
    count_1 = 0
    count_print = 1

    for i in reqsts_kpp:
        name_categories = i["name"]
        value_categories = i["value"]
        dict_category[f"{name_categories}"] = f"{value_categories}"
        if count_1 == 1000:
            break
        count_1 += 1
    for i in dict_category:
        a = f"{str(count_print)} - {i}"
        message = f"{message + a} \n"
        count_print += 1

    list_all.append(message)
    list_all.append(dict_category)

    return list_all


# pprint(test_kpp()[1])
