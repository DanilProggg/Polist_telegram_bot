
from aiogram.filters import BaseFilter
from aiogram.types import Message
import redisapi
from entity.User import deserialize

class AuthFilter(BaseFilter):
    async def __call__(self, message: Message):

        user = deserialize(redisapi.get_value(message.chat.id))
        if user.auth:
            return True
        else:
            return False
