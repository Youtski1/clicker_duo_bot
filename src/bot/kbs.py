from aiogram.types import InlineKeyboardButton as ibut
from aiogram.utils.keyboard import InlineKeyboardBuilder as builder


def kb_start():
    return builder([[
        ibut(text="Профиль",switch_inline_query_current_chat="/profile"),
        ibut(text="Играть",url="http://192.168.100.8:3000")
    ]]).adjust(2).as_markup()


def kb_profile():
    return builder([[
        ibut(text = "Повысить 🔫", callback_data="upgrade_damage")
    ]]).as_markup()