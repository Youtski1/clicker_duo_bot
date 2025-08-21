from aiogram import Router, F
from aiogram.types import CallbackQuery

from ...services import (
    UserService,
    DialogService
)

router = Router(name=__name__)


@router.callback_query(F.data == "upgrade_damage")
async def upgrade_damage(
    call: CallbackQuery,
    dialog_service: DialogService,
    user_service: UserService
):
    user = dialog_service.user
    if user.damage == 5:
        return

    status = await user_service.upgrade_damage(telegram_id=call.from_user.id)
    text = dialog_service.upgrade_damage(status=status)
    
    await call.answer(
        text=text,
        show_alert=True
    )