from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from aiohttp.client import ClientSession

from ..services import (
    UserService,
    DuoService,
    DialogService
)

class ServicesMiddleware(BaseMiddleware):

    def __init__(self, session: ClientSession):
        super().__init__()
        self.session = session

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        
        user_service = UserService(session=self.session)
        duo_service = DuoService(session=self.session)

        await user_service.upsert(
            telegram_id=event.from_user.id,
            full_name=event.from_user.full_name,
            username=event.from_user.username
        )

        await duo_service.insert(
            owner_id=event.from_user.id
        )

        duo = await duo_service.get_data(owner_id=event.from_user.id)
        user = await user_service.get_data(telegram_id=event.from_user.id)

        dialog_service = DialogService(
            user=user,
            duo=duo
        )

        data["user_service"] = user_service
        data["duo_service"] = duo_service
        data["dialog_service"] = dialog_service
        await handler(event, data)
            