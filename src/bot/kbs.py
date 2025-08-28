from aiogram.types import InlineKeyboardButton as ibut
from aiogram.utils.keyboard import InlineKeyboardBuilder as builder
from os import environ


LINK_WEB_APP = environ.get("LINK_WEB_URL")

def kb_start():
    return builder([[
        ibut(text="Профиль",switch_inline_query_current_chat="/profile"),
        ibut(text="Помощь", url="https://telegra.ph/Kak-bit-duo-08-21-2"),
        ibut(text="Играть",url=LINK_WEB_APP)
    ]]).adjust(2).as_markup()


def kb_profile():
    return builder([[
        ibut(text = "Повысить 🔫", callback_data="upgrade_damage")
    ]]).as_markup()