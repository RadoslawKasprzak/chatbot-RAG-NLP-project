import os
import openai

class ChatService:
    """
    A class that handles queries to OpenAI ChatGPT (model gpt-3.5-turbo or later).
    """
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.model_name = model_name
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_chat_response(self, conversation_context, user_message):
        """
        conversation_context - string containing the most important contexts (e.g. top_k chunks).
        user_message - user's question
        """
        system_message = {
            "role": "system",
            "content": (
                "Jesteś asystentem studenta - chatbotem, który pomaga studentom elki w znajdowaniu pomocny informacji ze strony wydziałowej. "
                "Wykorzystaj kontekst podany w system_prompt do odpowiedzi."
            )
        }

        # Możemy włączyć kontekst w 'system_prompt' lub osobnym 'assistant' message
        system_context = {
            "role": "assistant",
            "content": (
                f"Oto kontekst, który powinieneś wykorzystać:\n{conversation_context}\n"
                "Zasady: Odpowiadaj w oparciu o powyższe informacje. Masz dostęp tylko do tych informacji. Jeśli nie jesteś pewny odpowiedzi lub nie masz informacji na jakich możesz bazować to odpowiadaj: Nie znam odpowiedzi na to pytanie, odwiedź stronę https://www.elka.pw.edu.pl/ "
            )
        }

        user_message = {
            "role": "user",
            "content": user_message
        }

        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[system_message, system_context, user_message]
        )

        return response['choices'][0]['message']['content']
