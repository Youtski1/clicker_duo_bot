from .start_router import router as StartRouter
from .administrator_router import router as AdministratorRouter
from .setup import setup

all = [
    StartRouter,
    AdministratorRouter,
    setup
]