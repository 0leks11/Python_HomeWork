import logging
import redis
import openai
from telegram import Update
from telegram.ext import CallbackContext
from datetime import timedelta
import os
from dotenv import load_dotenv


# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение URL Redis и других переменных окружения
redis_url = os.getenv('REDIS_URL')

if not redis_url:
    raise ValueError("Переменная окружения REDIS_URL не определена")

# Настройка логирования
logger = logging.getLogger('handlers')

# Настройка Redis
r = redis.Redis.from_url(redis_url)

# Описание функций:
async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Доступные команды:\n"
        "/start - Начать новую сессию\n"
        "/stop - Завершить текущую сессию\n"
        "/restart - Сбросить текущий контекст\n"
        "/info - Информация о боте\n"
        "/help - Помощь"
    )
    await update.message.reply_text(help_text)
    logger.info("Помощь запрошена: %s", update.effective_chat.id)

async def info_command(update: Update, context: CallbackContext) -> None:
    info_text = (
        "Этот бот использует OpenAI для обработки сообщений и Redis для хранения контекста."
    )
    await update.message.reply_text(info_text)
    logger.info("Информация запрошена: %s", update.effective_chat.id)

async def restart_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    r.set(user_id, "[]")
    await update.message.reply_text('Контекст сброшен! Начата новая сессия.')
    logger.info("Контекст сброшен: %s", user_id)

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    r.setex(user_id, timedelta(minutes=30), "[]")
    await update.message.reply_text('Сессия начата!')
    logger.info("Сессия начата: %s", user_id)

async def stop(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    r.delete(user_id)
    await update.message.reply_text('Сессия завершена!')
    logger.info("Сессия завершена: %s", user_id)

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_message = update.message.text
    r.expire(user_id, timedelta(minutes=30))
    previous_context = eval(r.get(user_id) or "[]")
    previous_context.append({"role": "user", "content": user_message})

    try:
        logger.debug("Отправка запроса в OpenAI")
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=previous_context
        )

        bot_response = response['choices'][0]['message']['content']
        previous_context.append({"role": "assistant", "content": bot_response})
        r.setex(user_id, timedelta(minutes=30), str(previous_context))

        await update.message.reply_text(bot_response)
        logger.info("Ответ отправлен: %s - %s", user_id, bot_response)
    except Exception as e:
        logger.error("Ошибка при запросе к OpenAI: %s", e)
        await update.message.reply_text('Произошла ошибка при запросе к OpenAI.')

async def handle_photo(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    photo_file = await update.message.photo[-1].get_file()
    photo_path = f'temp/{photo_file.file_id}.jpg'
    await photo_file.download(photo_path)
    logger.debug("Фото загружено: %s", photo_path)
    r.expire(user_id, timedelta(minutes=30))
    previous_context = eval(r.get(user_id) or "[]")
    previous_context.append({"role": "user", "content": f'{update.message.caption}\n[photo]({photo_path})'})

    try:
        logger.debug("Отправка запроса в OpenAI с фото")
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=previous_context
        )
        
        bot_response = response['choices'][0]['message']['content']
        previous_context.append({"role": "assistant", "content": bot_response})
        r.setex(user_id, timedelta(minutes=30), str(previous_context))

        await update.message.reply_text(bot_response)
        logger.info("Фото обработано: %s", user_id)
    except Exception as e:
        logger.error("Ошибка при запросе к OpenAI: %s", e)
        await update.message.reply_text('Произошла ошибка при запросе к OpenAI.')

async def handle_document(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    document_file = await update.message.document.get_file()
    document_path = f'temp/{document_file.file_id}.pdf'
    await document_file.download(document_path)
    logger.debug("Документ загружен: %s", document_path)

    r.expire(user_id, timedelta(minutes=30))
    previous_context = eval(r.get(user_id) or "[]")
    previous_context.append({"role": "user", "content": f'{update.message.caption}\n[document]({document_path})'})

    try:
        logger.debug("Отправка запроса в OpenAI с документом")
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=previous_context
        )
        
        bot_response = response['choices'][0]['message']['content']
        previous_context.append({"role": "assistant", "content": bot_response})
        r.setex(user_id, timedelta(minutes=30), str(previous_context))

        await update.message.reply_text(bot_response)
        logger.info("Документ обработан: %s", user_id)
    except Exception as e:
        logger.error("Ошибка при запросе к OpenAI: %s", e)
        await update.message.reply_text('Произошла ошибка при запросе к OpenAI.')

async def handle_audio(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    audio_file = await update.message.audio.get_file()
    audio_path = f'temp/{audio_file.file_id}.mp3'
    await audio_file.download(audio_path)
    logger.debug("Аудио загружено: %s", audio_path)

    r.expire(user_id, timedelta(minutes=30))
    previous_context = eval(r.get(user_id) or "[]")
    previous_context.append({"role": "user", "content": f'{update.message.caption}\n[audio]({audio_path})'})

    try:
        logger.debug("Отправка запроса в OpenAI с аудио")
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=previous_context
        )
        
        bot_response = response['choices'][0]['message']['content']
        previous_context.append({"role": "assistant", "content": bot_response})
        r.setex(user_id, timedelta(minutes=30), str(previous_context))

        await update.message.reply_text(bot_response)
        logger.info("Аудио обработано: %s", user_id)
    except Exception as e:
        logger.error("Ошибка при запросе к OpenAI: %s", e)
        await update.message.reply_text('Произошла ошибка при запросе к OpenAI.')

async def handle_video(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    video_file = await update.message.video.get_file()
    video_path = f'temp/{video_file.file_id}.mp4'
    await video_file.download(video_path)
    logger.debug("Видео загружено: %s", video_path)

    r.expire(user_id, timedelta(minutes=30))
    previous_context = eval(r.get(user_id) or "[]")
    previous_context.append({"role": "user", "content": f'{update.message.caption}\n[video]({video_path})'})

    try:
        logger.debug("Отправка запроса в OpenAI с видео")
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=previous_context
        )
        bot_response = response['choices'][0]['message']['content']
        previous_context.append({"role": "assistant", "content": bot_response})
        r.setex(user_id, timedelta(minutes=30), str(previous_context))
        await update.message.reply_text(bot_response)
        logger.info("Видео обработано: %s", user_id)
    except Exception as e:
        logger.error("Ошибка при запросе к OpenAI: %s", e)
        await update.message.reply_text('Произошла ошибка при запросе к OpenAI.')