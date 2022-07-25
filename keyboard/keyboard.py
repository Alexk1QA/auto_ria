from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_Back_Menu = KeyboardButton("Главное меню")

keyboard_Back_Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_Back_Menu)

button_new = KeyboardButton("Новые")
button_BU = KeyboardButton("Б/У")

keyboard_NewOrBU = ReplyKeyboardMarkup(resize_keyboard=True).add(button_new, button_BU)
