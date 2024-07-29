import asyncio
import logging
from aiogram import F, Bot, Dispatcher, types

import handlers.start
import handlers.authorized
import secret

# Запуск процесса поллинга новых апдейтов
async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)

    # Объект бота
    bot = Bot(secret.token)

    # Диспетчер
    dp = Dispatcher()

    # Состояние юзера

    dp.include_routers(handlers.authorized.router, handlers.start.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())