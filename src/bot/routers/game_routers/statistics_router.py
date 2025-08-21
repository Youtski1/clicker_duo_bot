from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from ...kbs import *
from ...services import DialogService

router = Router(name=__name__)

@router.message(F.text == "@clicker_duo_bot /profile")
@router.message(F.text == "профиль")
@router.message(Command("profile"))
async def profile(
    message: Message,
    dialog_service: DialogService
):
    await message.answer(
        text=dialog_service.profile(),
        reply_markup=kb_profile()
    )


