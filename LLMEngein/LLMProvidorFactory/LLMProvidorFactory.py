from ..LLMEnums import LLMEnums
from ..LLMProvidor import OpenAIProvidor, GroqProvidor, OllamaProvidor, GminiProvidor
from dotenv import load_dotenv
import os
load_dotenv()




class LLMProvidorFactory():
    def __init__(self,llmProvidorName:str):
        self.llmProvidorName = llmProvidorName.strip()
        print(f"the providor is {self.llmProvidorName}")

    def GetLLMProvidor(self):
        if self.llmProvidorName == LLMEnums.OPENAI.value:
            return OpenAIProvidor().GetLLM()
        elif self.llmProvidorName == LLMEnums.GROQ.value:
            return GroqProvidor().GetLLM()
        elif self.llmProvidorName == LLMEnums.OLLAMA.value:
            return OllamaProvidor().GetLLM()
        elif self.llmProvidorName == LLMEnums.GEMINI.value:
            return GminiProvidor().GetLLM()
        else:
            raise ValueError("Invalid LLM Enum")