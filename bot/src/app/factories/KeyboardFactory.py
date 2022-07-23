from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.src.domain.repositories.MenuRepository import MenuRepository


def get_keyboard(language_code: str):
    menuKeys = MenuRepository().retrieve(language_code)

    btn_mon = KeyboardButton(menuKeys['mon'])
    btn_tue = KeyboardButton(menuKeys['tue'])
    btn_wed = KeyboardButton(menuKeys['wed'])
    btn_thu = KeyboardButton(menuKeys['thu'])
    btn_fri = KeyboardButton(menuKeys['fri'])
    btn_sat = KeyboardButton(menuKeys['sat'])
    btn_sun = KeyboardButton(menuKeys['sun'])

    return ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(btn_mon, btn_tue, btn_wed)\
        .row(btn_thu, btn_fri, btn_sat)\
        .row(btn_sun)
