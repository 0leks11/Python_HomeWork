import os
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import timedelta
import redis
from dotenv import load_dotenv

load_dotenv()

from handlers import (help_command, info_command, restart_command,
                      start, stop, handle_message, handle_photo,
                      handle_document, handle_audio, handle_video)

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
async def test_help_command(mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    await help_command(update, context)
    update.message.reply_text.assert_called_once()
    assert "Доступные команды" in update.message.reply_text.call_args[0][0]

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
async def test_info_command(mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    await info_command(update, context)
    update.message.reply_text.assert_called_once()
    assert "Этот бот использует OpenAI" in update.message.reply_text.call_args[0][0]

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
async def test_restart_command(mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    await restart_command(update, context)
    mock_redis.set.assert_called_once()
    update.message.reply_text.assert_called_once_with('Контекст сброшен! Начата новая сессия.')

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
async def test_start(mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    await start(update, context)
    mock_redis.setex.assert_called_once()
    update.message.reply_text.assert_called_once_with('Сессия начата!')

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
async def test_stop(mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    await stop(update, context)
    mock_redis.delete.assert_called_once()
    update.message.reply_text.assert_called_once_with('Сессия завершена!')

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
@patch('handlers.openai.ChatCompletion.create', new_callable=AsyncMock)
async def test_handle_message(mock_openai, mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    mock_openai.return_value = {
        'choices': [{'message': {'content': 'Mocked response from OpenAI'}}]
    }
    mock_redis.get.return_value = str([{"role": "user", "content": "previous message"}])
    await handle_message(update, context)
    update.message.reply_text.assert_called_once_with('Mocked response from OpenAI')
    mock_redis.setex.assert_called_once()

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
@patch('handlers.openai.ChatCompletion.create', new_callable=AsyncMock)
async def test_handle_photo(mock_openai, mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    mock_openai.return_value = {
        'choices': [{'message': {'content': 'Mocked response from OpenAI'}}]
    }
    mock_redis.get.return_value = str([{"role": "user", "content": "previous message"}])
    photo_file_mock = AsyncMock()
    photo_file_mock.download = AsyncMock()
    update.message.photo = [MagicMock(file_id="file_id_mock", get_file=AsyncMock(return_value=photo_file_mock))]
    update.message.caption = "Mock caption"
    await handle_photo(update, context)
    update.message.reply_text.assert_called_once_with('Mocked response from OpenAI')
    mock_redis.setex.assert_called_once()

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
@patch('handlers.openai.ChatCompletion.create', new_callable=AsyncMock)
async def test_handle_document(mock_openai, mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    mock_openai.return_value = {
        'choices': [{'message': {'content': 'Mocked response from OpenAI'}}]
    }
    mock_redis.get.return_value = str([{"role": "user", "content": "previous message"}])
    update.message.document = AsyncMock(file_id="file_id_mock")
    update.message.caption = "Mock caption"
    update.message.document.get_file.return_value = AsyncMock()
    await update.message.document.get_file.return_value.download(AsyncMock())
    await handle_document(update, context)
    update.message.reply_text.assert_called_once_with('Mocked response from OpenAI')
    mock_redis.setex.assert_called_once()

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
@patch('handlers.openai.ChatCompletion.create', new_callable=AsyncMock)
async def test_handle_audio(mock_openai, mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    mock_openai.return_value = {
        'choices': [{'message': {'content': 'Mocked response from OpenAI'}}]
    }
    mock_redis.get.return_value = str([{"role": "user", "content": "previous message"}])
    update.message.audio = AsyncMock(file_id="file_id_mock")
    update.message.caption = "Mock caption"
    update.message.audio.get_file.return_value = AsyncMock()
    await update.message.audio.get_file.return_value.download(AsyncMock())
    await handle_audio(update, context)
    update.message.reply_text.assert_called_once_with('Mocked response from OpenAI')
    mock_redis.setex.assert_called_once()

@pytest.mark.asyncio
@patch('handlers.r', autospec=True)
@patch('handlers.openai.ChatCompletion.create', new_callable=AsyncMock)
async def test_handle_video(mock_openai, mock_redis):
    update = AsyncMock()
    context = AsyncMock()
    mock_openai.return_value = {
        'choices': [{'message': {'content': 'Mocked response from OpenAI'}}]
    }
    mock_redis.get.return_value = str([{"role": "user", "content": "previous message"}])
    update.message.video = AsyncMock(file_id="file_id_mock")
    update.message.caption = "Mock caption"
    update.message.video.get_file.return_value = AsyncMock()
    await update.message.video.get_file.return_value.download(AsyncMock())
    await handle_video(update, context)
    update.message.reply_text.assert_called_once_with('Mocked response from OpenAI')
    mock_redis.setex.assert_called_once()