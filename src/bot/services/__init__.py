from .model_service.user_service import UserService
from .model_service.duo_service import DuoService
from .dialog_service import DialogService

all = [
    UserService,
    DuoService,
    DialogService
]