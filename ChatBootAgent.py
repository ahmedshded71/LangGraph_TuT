from langchain.agents import create_agent
from Schemas import State
from LLMEngein import LLMProvidorFactory
from Graphs import ChatAgentGraph


class ChatBootAgent():
    def __init__(self):
        self.llm = LLMProvidorFactory().GetLLM()
        self.agent = ChatAgentGraph()

    def Run(self,query:str):
        return self.agent.Run(query)
    
    def ViewGraph(self):
        return self.agent.ViewGraph()


if __name__ == "__main__":
    agent = ChatBootAgent()
    agent.ViewGraph()
    agent.Run("Hello, how what the latest AI news?")