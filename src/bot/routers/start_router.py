from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ..kbs import *


from ..services import (
    UserService,
    DuoService,
    DialogService
)


router = Router(name=__name__)


@router.message(CommandStart())
async def start(
    message: Message,
    dialog_service: DialogService
):
    await message.answer_photo(
        photo=dialog_service.avatar(),
        caption=dialog_service.start(),
        reply_markup=kb_start()
    )
