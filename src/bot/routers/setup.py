from aiogram import Dispatcher, Router

from . import (
    StartRouter,
    AdministratorRouter
)

from .game_routers import (
    StatisticsRouter,
    UpgradeRouter
)


from ..middlewaries import (
    AdministratorBotMiddleware
)

GameRouter = Router()
GameRouter.include_routers(
    StatisticsRouter,
    UpgradeRouter
)


def setup(dp: Dispatcher):
    dp.include_routers(
        StartRouter,
        AdministratorRouter,
        GameRouter
    )

    AdministratorRouter.message.middleware(AdministratorBotMiddleware())
    