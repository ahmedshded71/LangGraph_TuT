from ..LLMEnums import LLMEnums
from ..LLMProvidor import OpenAIProvidor, GroqProvidor, OllamaProvidor, GminiProvidor
from dotenv import load_dotenv
import os
load_dotenv()




class LLMProvidorFactory():
    def __init__(self,llmProvidorName:str):
        self.llmProvidorName = llmProvidorName

    def GetLLM(self):
        if self.llmProvidorName == LLMEnums.OPENAI:
            return OpenAIProvidor().GetLLM()
        elif self.llmProvidorName == LLMEnums.GROQ:
            return GroqProvidor().GetLLM()
        elif self.llmProvidorName == LLMEnums.OLLAMA:
            return OllamaProvidor().GetLLM()
        elif self.llmProvidorName == LLMEnums.GEMINI:
            return GminiProvidor().GetLLM()
        else:
            raise ValueError("Invalid LLM Enum")