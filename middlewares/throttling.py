import asyncio
import time

from aiogram import BaseMiddleware
from aiogram.types import Message

from typing import Callable, Dict, Any, Awaitable
from collections import defaultdict

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int =1.5):
        super().__init__()
        self.limit = limit
        self.last_time = defaultdict(float)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        now = time.time()

        if now - self.last_time[user_id] < self.limit:
            await event.answer("Too many requests! Please wait.")
            return 
        
        self.last_time[user_id] = now   
        return await handler(event, data)