from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_accept = KeyboardButton("Все понятно, можно начинать")
button_info = KeyboardButton("Детальное описание работы с ботом")

keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True).add(button_accept, button_info)

button_continued = KeyboardButton("Продолжить")

keyboard_button_continued = ReplyKeyboardMarkup(resize_keyboard=True).add(button_continued)

button_new = KeyboardButton("Новые")
button_BU = KeyboardButton("Б/У")

keyboard_NewOrBU = ReplyKeyboardMarkup(resize_keyboard=True).add(button_new, button_BU)

