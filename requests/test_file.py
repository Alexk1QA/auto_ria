import sqlite3
import requests
from dotenv import load_dotenv
import os
from route.route import *

load_dotenv()

# Данный участок кода возвращает список категорий и сожержимого категоий для наглядного понимания где, что находится
categories = requests.get("https://developers.ria.com/auto/categories/?api_key=0700hMiViMYsSFf6bhrG8nTK99LG9tKYEh4bwC1W").json()
for i in categories:
    categories1 = []
    name_categories = i["name"]
    value_categories = i["value"]
    categories1.append([name_categories, value_categories])
    print(f"/// /// /// {categories1} /// /// ///")

    reqsts_bodystyles = requests.get(f"https://developers.ria.com/auto/categories/{value_categories}/bodystyles?"
                                         f"api_key=0700hMiViMYsSFf6bhrG8nTK99LG9tKYEh4bwC1W").json()
    for i in reqsts_bodystyles:
        bodystyles1 = []
        nama_bodystyles = i["name"]
        value_bodystyles = i["value"]
        parentId_bodystyles = i["parentId"]
        bodystyles1.append([nama_bodystyles, value_bodystyles, parentId_bodystyles])
        print(f"--- {bodystyles1} ---")

# def categories():
#     # Функция возвращает список с словарями категорий
#
#     connect = sqlite3.connect("../data/categories.db")
#     cursor = connect.cursor()
#     reqsts_categories = requests.get(f"https://{url}{route_categories}?api_key={os.getenv('API_KEY')}").json()
#
#     cursor.execute(f"CREATE TABLE IF NOT EXISTS categories(name PRIMARI KEY TEXT,categories_id INTEGER)")
#     connect.commit()
#
#     for i in reqsts_categories:
#         name = i["name"]
#         value = i["value"]
#         add_column = f"ALTER TABLE categories ADD COLUMN '{name}'"
#         cursor.execute(add_column)
#         connect.commit()
#         # cursor.execute("INSERT INTO categories VALUES(?, ?);", [name, value])
#         # connect.commit()
#
#     return reqsts_categories


# categories()















