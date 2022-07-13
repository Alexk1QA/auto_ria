import requests
from dotenv import load_dotenv
import os

load_dotenv()


def req_category():
    categories = requests.get(f"https://developers.ria.com/auto/categories/1/"
                              f"marks?api_key={os.getenv('API_KEY')}").json()
    a = {}
    b = []
    c = 0
    for i in categories:
        name_categories = i["name"]
        value_categories = i["value"]
        b.append({name_categories, value_categories})
        a[f"{name_categories}"] = f"{value_categories}"
        if c == 1000:
            break
        c += 1
    finish = ""
    t = 0
    for i in a:
        finish = f"{finish + i} {t} \n"
        t += 1
    return finish
