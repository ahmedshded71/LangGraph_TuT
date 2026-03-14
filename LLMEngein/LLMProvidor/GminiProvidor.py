from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
from ..LLMInterface import LLMInterface

class GminiProvidor(LLMInterface):
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("GEMINI_MODEL_NAME"),
            temperature=0,
            api_key=os.getenv("GOOGLE_API_KEY")
        )

    def GetLLM(self):
        return self.llm