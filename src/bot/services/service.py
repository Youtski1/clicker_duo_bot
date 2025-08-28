from abc import ABC
from aiohttp.client import ClientSession

class BaseService:

    def __init__(
        self,
        session: ClientSession
    ):
        self.session = session
