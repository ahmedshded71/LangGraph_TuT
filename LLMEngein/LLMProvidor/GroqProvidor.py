from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from ..LLMInterface import LLMInterface

class GroqProvidor(LLMInterface):
    def __init__(self):
        self.llm = ChatGroq(
            model=os.getenv("GROQ_MODEL_NAME"),
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY")
        )

    def GetLLM(self):
        return self.llm