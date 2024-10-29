import openai
import asyncio
import logging
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import handlers

# Настройка логирования
logging.basicConfig(filename='bot.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    encoding='utf-8')
logger = logging.getLogger('main')

logger.debug('Debugging логирование начато.')

# Получение переменных окружения
openai.api_key = os.getenv('OPENAI_API_KEY')
telegram_token = os.getenv('TELEGRAM_TOKEN')
redis_url = os.getenv('REDIS_URL')

if not all([openai.api_key, telegram_token, redis_url]):
    logger.error('Не все переменные окружения установлены.')
    raise ValueError('Не все переменные окружения установлены.')

logger.debug(f"OpenAI API Key Loaded: {openai.api_key}")
logger.debug(f"Telegram Token Loaded: {telegram_token}")
logger.debug(f"Redis URL Loaded: {redis_url}")

# Главная функция для запуска бота
async def main() -> None:
    logger.debug("Инициализация приложения")

    app = ApplicationBuilder().token(telegram_token).build()

    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("help", handlers.help_command))
    app.add_handler(CommandHandler("info", handlers.info_command))
    app.add_handler(CommandHandler("restart", handlers.restart_command))
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("stop", handlers.stop))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handlers.handle_photo))
    app.add_handler(MessageHandler(filters.Document.ALL, handlers.handle_document))
    app.add_handler(MessageHandler(filters.AUDIO, handlers.handle_audio))
    app.add_handler(MessageHandler(filters.VIDEO, handlers.handle_video))

    logger.info('Бот запущен и готов к работе.')

    try:
        # Инициализация и запуск бота
        await app.initialize()
        logger.debug("Инициализация завершена")

        await app.start()
        logger.debug("Бот запущен")
        logger.debug("Запуск polling")
        await app.run_polling()

        logger.debug("Бот готов к работе")
        await app.idle()
    except Exception as e:
        logger.error(f"Ошибка во время запуска бота: {e}")

if __name__ == '__main__':
    logger.debug('Запуск главного скрипта')
    try:
        if asyncio.get_event_loop().is_running():
            # Используем другой метод запуска main()
            asyncio.ensure_future(main())
        else:
            asyncio.run(main())
    except Exception as e:
           logger.error(f"Ошибка при запуске main: {e}")








        