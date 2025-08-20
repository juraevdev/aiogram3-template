import logging
from aiogram.types import Update
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramForbiddenError,
    TelegramUnauthorizedError,
    TelegramRetryAfter,
    TelegramNetworkError
)

from loader import dp


async def errors_handler(update: Update, exception: Exception):
    if isinstance(exception, TelegramUnauthorizedError):
        logging.exception(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, TelegramRetryAfter):
        logging.exception(f'RetryAfter: {exception}')
        return True

    if isinstance(exception, TelegramBadRequest):
        logging.exception(f'Bad Request: {exception}')
        return True

    if isinstance(exception, TelegramForbiddenError):
        logging.exception(f'Forbidden: {exception}')
        return True

    if isinstance(exception, TelegramNetworkError):
        logging.exception(f'Network Error: {exception}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
    return True


dp.errors.register(errors_handler)
