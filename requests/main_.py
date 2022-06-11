import sqlite3
import requests
from dotenv import load_dotenv
import os
from route.route import *

load_dotenv()

# по файлм
# юзерагент
# return
# env

# вернуть списком в любом случае

def categories():
    # Функция возвращает список с словарями категорий

    connect = sqlite3.connect("../data/categories.db")
    cursor = connect.cursor()
    reqsts_categories = requests.get(f"https://{url}{route_categories}?api_key={os.getenv('API_KEY')}").json()

    cursor.execute("""CREATE TABLE IF NOT EXISTS categories2(
    category PRIMARI KEY TEXT,
    categories_id INTEGER
    )""")
    connect.commit()

    for i in reqsts_categories:
        name = i["name"]
        value = i["value"]
        cursor.execute("INSERT INTO categories2 VALUES(?, ?);", [name, value])
        connect.commit()

    return reqsts_categories


def bodystyles():
    connect = sqlite3.connect("../data/categories.db")
    cursor = connect.cursor()

    for i in categories():
        name_categories = i["name"]
        value_categories = i["value"]
        print(name_categories, value_categories)
        reqsts_bodystyles = requests.get(f"https://{url}{route_categories}/{value_categories}/{route_bodystyles}"
                                         f"?api_key={os.getenv('API_KEY')}").json()



        for i in reqsts_bodystyles:
            nama_bodystyles = i["name"]
            value_bodystyles = i["value"]
            parentId_bodystyles = i["parentId"]

            cursor.execute(f"""CREATE TABLE IF NOT EXISTS bodystyles(
            
            name_bodystyles_{value_categories} PRIMARI KEY TEXT,
            value_bodystyles_{value_categories} INTEGER,
            parentId_bodystyles_{value_categories} INTEGER,
            
            )""")


            cursor.execute("INSERT INTO bodystyles VALUES(?, ?, ?);", [nama_bodystyles, value_bodystyles, parentId_bodystyles])
            connect.commit()

        return reqsts_bodystyles


        # cursor.execute(""" CREATE TABLE IF NOT EXISTS all_bodystyles(
        #         bodystyles TEXT,
        #         categories_id INTEGER,
        #         parentId TEXT
        #     )""")
        # connect.commit()
        #
        # for i in reqsts_bodystyles:
        #     name = i["name"]
        #     value = i["value"]
        #     parentId = i["parentId"]
        #     cursor.execute("INSERT INTO bodystyles VALUES(?, ?, ?);", [name, value, parentId])
        #     connect.commit()

# print(bodystyles())

# nama_bodystyles = 1
# value_bodystyles = 2
# parentId_bodystyles = 3









def marks():
    connect = sqlite3.connect("marks.db")
    cursor = connect.cursor()
    requests_ = requests.get("https://developers.ria.com/auto/categories/1/marks?"
                             "api_key=0700hMiViMYsSFf6bhrG8nTK99LG9tKYEh4bwC1W").json()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS marks(
        marka TEXT,
        marka_id INTEGER
    )""")
    connect.commit()

    for i in requests_:
        name = i["name"]
        value = i["value"]
        cursor.execute("INSERT INTO marks VALUES(?, ?);", [name, value])
        connect.commit()


def model():
    connect = sqlite3.connect("model.db")
    cursor = connect.cursor()
    requests_ = requests.get("https://developers.ria.com/auto/categories/1/marks/9/models?"
                             "api_key=0700hMiViMYsSFf6bhrG8nTK99LG9tKYEh4bwC1W").json()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS model(
        marka TEXT,
        marka_id INTEGER
    )""")
    connect.commit()

    for i in requests_:
        name = i["name"]
        value = i["value"]
        cursor.execute("INSERT INTO model VALUES(?, ?);", [name, value])
        connect.commit()




# marks()
# model()
