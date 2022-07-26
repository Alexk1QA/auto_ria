import requests
global transport_type, region


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.0.0 Safari/537.36"
}

# типы транспорта
def type_used_cars():
    transport_type = (requests.get("https://developers.ria.com/auto/categories/?api_key=MvwyZnYWyRXWAhv4Y6jox89jd5"
                                   "0F4XAJH5UEzGR0", headers=headers)).json()
    return transport_type

print(type_used_cars())


# типы кузова
def car_body_types():
    transport_type = (requests.get("https://developers.ria.com/auto/categories/gearboxes?"
                                   "api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0", headers=headers)).json()
    result_bodytypes = dict()
    for items in transport_type:
        id = items["value"]
        name = items["name"]
        bodytypes = requests.get(f"https://developers.ria.com/auto/categories/{id}/bodystyles?api_key=Mvw"
                                        f"yZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0", headers=headers).json()
        for items in bodytypes:
            id_bodycar = items["value"]
            result_bodytypes[items['name']] = id_bodycar
    return result_bodytypes

print(car_body_types())


# марки авто
def car_brand():
    transport_type = (requests.get("https://developers.ria.com/auto/categories/gearboxes?"
                                   "api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0", headers=headers)).json()
    result_brands = dict()
    for items in transport_type:
        id = items["value"]
        name = items["name"]
        brands = requests.get(f"https://developers.ria.com/auto/categories/{id}/marks?api_key=MvwyZnYWyRXWAhv4Y"
                              f"6jox89jd50F4XAJH5UEzGR0", headers=headers).json()
        for items in brands:
            id_brand = items["value"]
            result_brands[items['name']] = id_brand
    return result_brands

print(car_brand())


# модели авто
def models_used_auto():







# области
def regions():
    region = requests.get(f"https://developers.ria.com/auto/states?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0",
                          headers=headers).json()
    return region

print(regions())




# города
def cities():
    region = requests.get(f"https://developers.ria.com/auto/states?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0",
                          headers=headers).json()
    result_regions = dict()
    for items in region:
        region_id = items["value"]
        region_name = items["name"]
        city = requests.get(
            f"https://developers.ria.com/auto/states/{region_id}/cities?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0",
            headers=headers).json()
        for items in city:
            id_city = items["value"]
            result_regions[items['name']] = id_city
    return result_regions
print(cities())



# типы привода
def drive_types():
    for items in transport_type:
        transport_id = items["value"]
        drives_type = requests.get(f"https://developers.ria.com/auto/categories/{transport_id}/driverTypes?"
                                    f"api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0", headers=headers).json()
        if len(drives_type) == 0:
            return f"Привода в {items['name']} нет !"
        else:
            return drives_type

print(drive_types())



# типы топлива
def fuel_types():
    fuel_type = requests.get(f"https://developers.ria.com/auto/type?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0",
                             headers=headers).json()
    return fuel_type

print(fuel_types())



# коробки передач
def gearboxes():
    for items in transport_type:
        id = items["value"]
        name = items["name"]
        url_gearbox = f"https://developers.ria.com/auto/categories/{id}/gearboxes?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4" \
                      f"XAJH5UEzGR0"
        gearbox_type = requests.get(f"{url_gearbox}", headers=headers)
        result_gearbox = gearbox_type.json()
        if len(result_gearbox) == 0:
            return f"Коробок передач у {name} нет!"
        else:
            return result_gearbox

print(gearboxes())



# опции
def options():
    for items in transport_type:
        id = items["value"]
        name = items["name"]
        url_options = f"https://developers.ria.com/auto/categories/{id}/options?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH" \
                      f"5UEzGR0"
        options_type = requests.get(f"{url_options}", headers=headers)
        result_options = options_type.json()
        if len(result_options) == 0:
            return f"Коробок передач у {name} нет!"
        else:
            return result_options

print(options())



# цвета
def colors():
    url_colors = "https://developers.ria.com/auto/colors?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0"
    colors = requests.get(f"{url_colors}", headers=headers)
    result_colors = colors.json()
    return result_colors

print(colors())



# страна производитель
def producing_country():
    url_countries = "https://developers.ria.com/auto/countries?api_key=MvwyZnYWyRXWAhv4Y6jox89jd50F4XAJH5UEzGR0"
    countries = requests.get(f"{url_countries}", headers=headers)
    result_countries = countries.json()
    return result_countries

print(producing_country())
