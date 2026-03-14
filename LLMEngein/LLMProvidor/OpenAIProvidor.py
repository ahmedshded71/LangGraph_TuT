from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
from ..LLMInterface import LLMInterface

class OpenAIProvidor(LLMInterface):
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL_NAME"),
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def GetLLM(self):
        return self.llm