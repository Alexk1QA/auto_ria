import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.0.0 Safari/537.36"
}


# типа транспорта
def type_new_cars():
    transport_type = (requests.get("https://developers.ria.com/auto/categories/?api_key=MvwyZnYWyRXWAhv4Y6jox89jd5"
                                   "0F4XAJH5UEzGR0", headers=headers)).json()
    return transport_type


print(type_new_cars())

result_brands = dict()


# марка авто
def brand_new_cars():
    transport_type = (requests.get("https://developers.ria.com/auto/categories/?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F"
                                   "4XAJH5UEzGR0", headers=headers)).json()
    for items in transport_type:
        id = items["value"]
        name = items["name"]
        brands = requests.get(f"https://developers.ria.com/auto/new/marks?category_id={id}&api_key=MvwyZnYWyRXWAhv4Y"
                              f"6jox89jd50F4XAJH5UEzGR0", headers=headers).json()
        for items in brands:
            id_brand = items["value"]
            result_brands[items['name']] = id_brand
    return result_brands


print(brand_new_cars())


# модели
def models():
    result_models = dict()
    for items in result_brands.keys():
        id_brand = items["marka_id"]
        url_models = f"https://developers.ria.com/auto/new/models?marka_id={id_brand}&category_id=id&api_key=MvwyZnYWyRX" \
                     f"WAhv4Y6jox89jd50F4XAJH5UEzGR0"
        models = requests.get(f"{url_models}", headers=headers).json()
        for items in models:
            name_model = items["name"]
            id_marka = items["marka_id"]
            result_models[items['name']] = id_marka
    return result_models


print(models())
