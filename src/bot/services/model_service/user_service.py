from aiohttp.client import ClientSession
from ...types import User
from dotenv import load_dotenv
from os import environ
from ..service import BaseService   

load_dotenv()

import logging


API_URL = environ.get("API_URL")
API_KEY = environ.get("API_KEY")

logger = logging.getLogger(__name__)


class UserService(BaseService): 

    async def get_data(
        self,
        telegram_id: int
    ):
        async with self.session.get(
            url=f"{API_URL}user/{telegram_id}",
            headers={"api-key": API_KEY}
        ) as response:
            status_response = response.status
            
            if status_response == 200:
                logger.info("user data received")
                data = await response.json()
                return User(**data["user"])
            
            logger.info("not user data")
            
            
    async def upsert(
        self,
        telegram_id: int,
        full_name: str,
        username: str
    ):
        async with self.session.post(
            url=f"{API_URL}user/upsert_user",
            json={
                'telegram_id': telegram_id,
                'full_name': full_name,
                'username': username
            },
            headers={'api-key': API_KEY}
        ) as response:
            status_response = response.status
            text_response = await response.text()
            
            logger.info(f" {text_response} : status: {status_response}")
        
    async def upgrade_damage(
        self,
        telegram_id: int
    ):
        user = await self.get_data(telegram_id=telegram_id)
        feathers_count = user.damage * 300 + 900
        
        if user.feathers < feathers_count:
            return False

        async with self.session.post(
            url=f"{API_URL}user/upgrade_damage",
            json={
                "telegram_id": telegram_id,
                "feathers_count": feathers_count
            },
            headers={'api-key': API_KEY}
        ) as response:
            status_response = response.status
            text_response = await response.text()
            logger.info(f"{text_response} :  status: {status_response}")

            if status_response == 200:
                return True
            
