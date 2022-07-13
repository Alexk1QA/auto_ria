from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_2_Param = KeyboardButton("2 параметра")
button_5_Param = KeyboardButton("5 параметров")

keyboard_Params = ReplyKeyboardMarkup(resize_keyboard=True).add(button_2_Param, button_5_Param)

button_Lehkovie = KeyboardButton("Легковые")
button_Moto = KeyboardButton("Мото")
button_VodniyTransport = KeyboardButton("Водный транспорт")
button_SpecTehnika = KeyboardButton("Спецтехника")
button_Pricepi = KeyboardButton("Прицепы")
button_Gruzoviki = KeyboardButton("Грузовики")
button_Avtobusu = KeyboardButton("Автобусы")
button_AvtoDoma = KeyboardButton("Автодома")
button_VozdushniyTransport = KeyboardButton("Воздушный транспорт")
button_SelhozTehnika = KeyboardButton("Сельхозтехника")

keyboard_category = ReplyKeyboardMarkup(resize_keyboard=True).add(button_Lehkovie, button_Moto, button_VodniyTransport,
                                                                  button_SpecTehnika, button_Pricepi, button_Gruzoviki,
                                                                  button_Avtobusu, button_AvtoDoma,
                                                                  button_VozdushniyTransport, button_SelhozTehnika)

button_bmw = KeyboardButton("bmw")
button_audi = KeyboardButton("audi")
button_mercedes_benz = KeyboardButton("mercedes-benz")
button_volkswagen = KeyboardButton("volkswagen")
button_toyota = KeyboardButton("toyota")
button_skoda = KeyboardButton("skoda")
button_honda = KeyboardButton("honda")
button_ford = KeyboardButton("ford")
button_hyundai = KeyboardButton("hyundai")
button_chevrolet = KeyboardButton("chevrolet")
button_kia = KeyboardButton("kia")
button_lexus = KeyboardButton("lexus")
button_mazda = KeyboardButton("mazda")
button_nissan = KeyboardButton("nissan")
button_mitsubishi = KeyboardButton("mitsubishi")
button_back = KeyboardButton("Назад")

keyboard_topMarks_Lehkovie = ReplyKeyboardMarkup(resize_keyboard=True).add(button_bmw, button_audi,
                                                                           button_mercedes_benz, button_volkswagen,
                                                                           button_toyota, button_skoda, button_honda,
                                                                           button_ford, button_hyundai,
                                                                           button_chevrolet, button_kia, button_lexus,
                                                                           button_mazda, button_nissan,
                                                                           button_mitsubishi, button_back)

button_bmw = KeyboardButton("bmw")
button_brp = KeyboardButton("brp")
button_ducati = KeyboardButton("ducati")
button_harley_davidson = KeyboardButton("harley-davidson")
button_honda = KeyboardButton("honda")
button_kawasaki = KeyboardButton("kawasaki")
button_ktm = KeyboardButton("ktm")
button_suzuki = KeyboardButton("suzuki")
button_yamaha = KeyboardButton("yamaha")
button_aprilia = KeyboardButton("aprilia")
button_zongshen = KeyboardButton("zongshen")
button_viper = KeyboardButton("viper")
button_triumph = KeyboardButton("triumph")
button_loncin = KeyboardButton("loncin")
button_kovi = KeyboardButton("kovi")

keyboard_topMarks_Moto = ReplyKeyboardMarkup(resize_keyboard=True).add(button_bmw, button_brp, button_ducati,
                                                                       button_harley_davidson, button_honda,
                                                                       button_kawasaki, button_ktm, button_suzuki,
                                                                       button_yamaha, button_aprilia, button_zongshen,
                                                                       button_viper, button_triumph, button_loncin,
                                                                       button_kovi)

button_bayliner = KeyboardButton("bayliner")
button_brp = KeyboardButton("brp")
button_finval = KeyboardButton("finval")
button_honda = KeyboardButton("honda")
button_yamaha = KeyboardButton("yamaha")
button_kawasaki = KeyboardButton("kawasaki")
button_suzuki = KeyboardButton("suzuki")
button_toyota = KeyboardButton("toyota")
button_jaguar = KeyboardButton("jaguar")

keyboard_topMarks_VodniyTransport = ReplyKeyboardMarkup(resize_keyboard=True).add(button_bayliner, button_brp,
                                                                                  button_finval, button_honda,
                                                                                  button_yamaha, button_kawasaki,
                                                                                  button_suzuki, button_toyota,
                                                                                  button_jaguar)
