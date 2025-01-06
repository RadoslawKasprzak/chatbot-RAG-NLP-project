import os
import openai

class ChatService:
    """
    A class that handles queries to OpenAI ChatGPT (model gpt-3.5-turbo or later).
    """
    def __init__(self, 
                model_name: str = "gpt-3.5-turbo",
                system_prompt_file: str = "prompts/system_prompt.txt",
                assistant_prompt_file: str = "prompts/assistant_prompt.txt",
        ):
        self.model_name = model_name
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # Wczytaj plik system_prompt.txt
        with open(system_prompt_file, "r", encoding="utf-8") as f:
            self.system_prompt = f.read().strip()

        # Wczytaj plik assistant_prompt.txt
        with open(assistant_prompt_file, "r", encoding="utf-8") as f:
            self.assistant_prompt = f.read().strip()

    def get_chat_response(self, conversation_context, user_message):
        """
        conversation_context - string containing the most important contexts (e.g. top_k chunks).
        user_message - user's question
        """
        system_message = {
            "role": "system",
            "content": self.system_prompt
        }

        assistant_text = self.assistant_prompt.format(
            conversation_context=conversation_context
        )

        # Możemy włączyć kontekst w 'system_prompt' lub osobnym 'assistant' message
        system_context = {
            "role": "assistant",
            "content": assistant_text
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
