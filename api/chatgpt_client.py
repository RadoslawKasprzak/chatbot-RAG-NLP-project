import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    def __init__(self, model: str = "gpt-4"):
        """
        Initializes the OpenAI client.

        Args:
            model (str): The model to use (e.g., 'gpt-4').
        """
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("OpenAI API key is required.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    def chat(self, user_message: str, system_message: str = None, temperature: float = 0.7, max_tokens: int = 500):
        """
        Sends a chat request to the GPT model.

        Args:
            user_message (str): The message from the user.
            system_message (str): Optional system message to define the context.
            temperature (float): Controls creativity of the response (0-1).
            max_tokens (int): The maximum number of tokens in the response.

        Returns:
            str: The response from the GPT model.
        """
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": user_message})

        try:
            # Call the API
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens
            )

            # Access the response content
            return response.choices[0].message.content

        except Exception as e:
            raise RuntimeError(f"Error while communicating with OpenAI: {e}")

    def summarize(self, text: str, temperature: float = 0.5, max_tokens: int = 100):
        """
        Summarizes the provided text using GPT.

        Args:
            text (str): The text to summarize.
            temperature (float): Controls creativity of the response (0-1).
            max_tokens (int): The maximum number of tokens in the response.

        Returns:
            str: The summary of the text.
        """
        system_message = "You are a helpful assistant that summarizes text."
        return self.chat(
            user_message=f"Please summarize the following text: {text}",
            system_message=system_message,
            temperature=temperature,
            max_tokens=max_tokens
        )