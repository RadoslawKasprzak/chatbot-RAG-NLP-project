import pytest
from unittest.mock import patch
from services.chat_service import ChatService

@patch("services.chat_service.openai.ChatCompletion.create")
def test_chat_response(mock_openai):
    mock_openai.return_value = {
        "choices": [
            {
                "message": {"content": "Testowa odpowiedź GPT"}
            }
        ]
    }

    chat_svc = ChatService(model_name="gpt-3.5-turbo")
    context = "Jakiś kontekst chunków"
    user_msg = "Jakieś pytanie usera"
    response = chat_svc.get_chat_response(context, user_msg)

    assert response == "Testowa odpowiedź GPT"
    mock_openai.assert_called_once()
