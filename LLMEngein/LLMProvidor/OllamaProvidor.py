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
            api_key=os.getenv("OLLAMA_API_KEY")
        )

    def GetLLM(self):
        return self.llm