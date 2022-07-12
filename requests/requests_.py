import requests
from dotenv import load_dotenv
import os
from route.route import *

global c

load_dotenv()


def categories():
    # Функция возвращает список все типы категорий
    reqsts_categories = requests.get(f"https://{url}{route_categories}?api_key={os.getenv('API_KEY')}").json()

    return reqsts_categories


def bodystyles():
    # Функция возвращает список с типом кузовов всех категорий

    bodystyles = {}

    for i in categories():
        name_categories = i["name"]
        value_categories = i["value"]
        reqsts_bodystyles = requests.get(f"https://{url}{route_categories}/{value_categories}/{route_bodystyles}"
                                         f"?api_key={os.getenv('API_KEY')}").json()

        bodystyles[f"{name_categories}"] = f"{reqsts_bodystyles}"

    return bodystyles


def marks():
    # Функция возвращает список с всеми марками

    marks = {}

    for i in categories():
        name_categories = i["name"]
        value_categories = i["value"]
        reqsts_bodystyles = requests.get(f"https://{url}{route_categories}/{value_categories}/{route_marks}"
                                         f"?api_key={os.getenv('API_KEY')}").json()

        marks[f"{name_categories}"] = f"{reqsts_bodystyles}"

    return marks


# pprint(marks())

# ii = 0
# for i in marks():
#     print(i)
#     if ii == 100:
#         break
#     ii =+ 1


def models():
    # Функция возвращает список с всеми марками

    models = {}

    for i in categories():
        name_categories = i["name"]
        value_categories = i["value"]

        marks_dic = marks()

        for ii in marks_dic.items():
            for iii in ii:
                if iii == list:
                    break
                print(iii)
                print("---" * 30)

            # reqsts_bodystyles = requests.get(f"https://{url}{route_categories}/{value_categories}/{route_marks}"
            #                                  f"?api_key={os.getenv('API_KEY')}").json()
            #
            # models[f"{name_categories}"] = f"{reqsts_bodystyles}"

    return models


print(models())
