import redis
import os
import logging

from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

redis_url = os.getenv('REDIS_URL')

# Настройка логирования
logger = logging.getLogger('redis_helper')

def init_redis_connection():
    try:
        r = redis.Redis.from_url(redis_url)
        r.ping()
        logger.info(f"Подключение к Redis установлено: {redis_url}")
        return r
    except redis.ConnectionError as e:
        logger.error(f"Ошибка при подключении к Redis: {e}")
        return None

r = init_redis_connection()