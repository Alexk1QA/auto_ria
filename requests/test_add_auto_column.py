import sqlite3
import requests
from dotenv import load_dotenv
import os
from route.route import *

global reqsts_bodystyles

load_dotenv()

# по файлм
# юзерагент
# return
# env

# вернуть списком в любом случае


def categories():
    # Функция возвращает список с словарями категорий

    connect = sqlite3.connect("../data/auto.db")
    cursor = connect.cursor()
    reqsts_categories = requests.get(f"https://{url}{route_categories}?api_key={os.getenv('API_KEY')}").json()

    cursor.execute("""CREATE TABLE IF NOT EXISTS categories(
    category PRIMARY KEY ,
    categories_id INTEGER
    )""")
    connect.commit()

    for i in reqsts_categories:
        print(i)
        name = i["name"]
        value = i["value"]
        cursor.execute("INSERT INTO categories VALUES(?, ?);", [name, value])
        connect.commit()

    return reqsts_categories

categories()

def bodystyles2():
    global reqsts_bodystyles
    # Функция возвращает список с словарями категорий

    connect = sqlite3.connect("../data/categories.db")
    cursor = connect.cursor()

    cursor.execute(f"CREATE TABLE IF NOT EXISTS bodystyles(id INTEGER AUTO INCREMENT PRIMARY KEY)")

    connect = sqlite3.connect("/test/auto.db")

    "sqlite3 ./folderName/databaseName.db"
    connect.commit()


    q = 0

    for i in categories():
        print(i)
        name_categories = i["name"]
        value_categories = i["value"]
        add_column_1 = f"ALTER TABLE bodystyles ADD COLUMN 'type_{value_categories}'"
        cursor.execute(add_column_1)
        add_column_2 = f"ALTER TABLE bodystyles ADD COLUMN 'value_{value_categories}'"
        cursor.execute(add_column_2)
        add_column_3 = f"ALTER TABLE bodystyles ADD COLUMN 'parentid_{value_categories}'"
        cursor.execute(add_column_3)
        connect.commit()

        print("-")

        reqsts_bodystyles = requests.get(f"https://{url}{route_categories}/{value_categories}/{route_bodystyles}"
                                         f"?api_key={os.getenv('API_KEY')}").json()

        # sql.execute("SELECT Название столбца FROM Название Таблицы")

        for i in reqsts_bodystyles:
            name = i["name"]
            value = i["value"]
            parentid = i["parentId"]
            if q == 0:
                cursor.execute("INSERT INTO bodystyles VALUES(?, ?, ?, ?);", [q, name, value, parentid])
                connect.commit()
            # else:
            #
            #     cursor.execute("INSERT INTO bodystyles VALUES(?, ?, ?);", [name, value, parentid])
            #     connect.commit()
            # print("--")

        # for i in reqsts_bodystyles:
        #     name = i["name"]
        #     value = i["value"]
        #     parentid = i["parentId"]
        #     if q == 0:
        #
        #         cursor.execute("INSERT INTO bodystyles VALUES(?, ?, ?, ?);", [q, name, value, parentid])
        #         connect.commit()
        #     else:
        #         cursor.execute("INSERT INTO bodystyles VALUES(?, ?, ?);", [name, value, parentid])
        #         connect.commit()
        #     print("--")

        q += 1
    return reqsts_bodystyles

# bodystyles2()

