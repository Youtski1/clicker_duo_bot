from ..service import BaseService
from os import environ
import logging

from ...types import Duo


API_URL = environ.get("API_URL")
API_KEY = environ.get("API_KEY")

logger = logging.getLogger(__name__)

class DuoService(BaseService):

    async def insert(
        self,
        owner_id: int
    ):
        duo = await self.get_data(owner_id=owner_id)
        
        if duo:
            logger.info("alreade have duo")
            return 
        
        async with self.session.post(
            url=f"{API_URL}duo/new_duo",
            json={'owner_id': owner_id},
            headers={'api-key': API_KEY}
        ) as response:
            status_response = response.status
            text_response = await response.text()

            logger.info(f"{text_response} : status: {status_response}")
    
    
    async def get_data(
        self,
        owner_id: int
    ):
        async with self.session.get(
            url=f"{API_URL}duo/{owner_id}",
            headers={'api-key': API_KEY}
        ) as response:
            status_response = response.status   

            if status_response == 200:
                logger.info("duo data received")
                data = await response.json()
                return Duo(**data["duo"])
            
            logger.info("not duo data")