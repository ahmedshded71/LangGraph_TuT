from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
load_dotenv()
from ..LLMInterface import LLMInterface
class OllamaProvidor(LLMInterface):
    def __init__(self):
        self.llm = ChatOllama(
                    model=os.getenv("OLLAMA_MODEL_NAME"),
                    temperature=0,
                    base_url=os.getenv("OLLAMA_API_KEY"), # هنا نضع رابط ngrok
                    client_kwargs={
                        "headers": {
                            "ngrok-skip-browser-warning": "true",
                            "Content-Type": "application/json"
                        }
                    }
                )

    def GetLLM(self):
        return self.llm