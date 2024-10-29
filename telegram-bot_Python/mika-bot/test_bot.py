import pytest
from unittest.mock import AsyncMock, patch
from bot import create_application, main
from telegram.ext import CommandHandler
from telegram.ext import ApplicationBuilder
from unittest.mock import AsyncMock, patch

# Test for create_application
def test_create_application():
    app = create_application()

    # Проверка, что атрибут handlers существует и является словарем
    assert hasattr(app, 'handlers')
    assert isinstance(app.handlers, dict), f"Expected 'handlers' to be a dict, got {type(app.handlers)}"

    # Подсчет общего количества обработчиков во всех группах
    handlers_count = sum(len(handler_group) for handler_group in app.handlers.values())
    assert handlers_count == 10, f"Expected 10 handlers, but got {handlers_count}"

    # Проверка правильной настройки командных обработчиков
    command_handlers = [
        h for handler_group in app.handlers.values()
        for h in handler_group if isinstance(h, CommandHandler)
    ]
    commands = [cmd.command for cmd in command_handlers]
    expected_commands = ["/help", "/info", "/restart", "/start", "/stop"]
    assert all(cmd in commands for cmd in expected_commands), "Not all expected commands were found"


# Test for main
import pytest
from unittest.mock import AsyncMock, Mock, patch

@pytest.mark.asyncio
@patch('bot.create_application', new_callable=AsyncMock)
@patch('bot.asyncio.run', new_callable=AsyncMock)
async def test_main():
    with patch.object(ApplicationBuilder, 'token', new_callable=AsyncMock) as mock_token, \
        patch('bot.ApplicationBuilder') as mock_app_builder, \
        patch('bot.handlers') as mock_handlers:

        mock_app = mock_app_builder.return_value
        mock_app.initialize = AsyncMock()
        mock_app.run = AsyncMock()
        mock_app.run_polling = AsyncMock()
        mock_app.idle = AsyncMock()
        
        await main()

        mock_app_builder.assert_called_once()
        mock_app_builder.return_value.token.assert_called_once_with('EMAIL_TOKEN_HERE')
        
        # Проверяем, что бот был инициализирован и запущен
        mock_app.initialize.assert_called_once()
        mock_app.run.assert_called_once()
        mock_app.run_polling.assert_called_once()
        mock_app.idle.assert_called_once()



