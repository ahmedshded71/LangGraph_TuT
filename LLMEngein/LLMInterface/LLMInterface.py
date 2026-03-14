from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def GetLLM(self):
        pass
