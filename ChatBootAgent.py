from langchain.agents import create_agent
from Schemas import State
from LLMEngein import LLMProvidorFactory
from Graphs import ChatAgentGraph
import os


class ChatBootAgent():
    def __init__(self):
        self.agent = ChatAgentGraph()

    def Run(self,query:str):
        return self.agent.Run(query)
    

    
    def ViewGraph(self):
        return self.agent.ViewGraph()


if __name__ == "__main__":
    agent = ChatBootAgent()
    agent.ViewGraph()
    result=agent.Run("Hello, how what the latest  trendy paper in agentic ai with network?")
    print("\n" + "="*50)
    print("📌 AGENTIC AI EXECUTION TRACE")
    print("="*50 + "\n")

    for msg in result["messages"]:
        role = msg.__class__.__name__.replace("Message", "").upper()
        
        if role == "HUMAN":
            print(f"👤 USER: {msg.content}\n")
        
        elif role == "AI":
            if msg.tool_calls:
                for tool in msg.tool_calls:
                    print(f"🤖 AI DECISION: Calling Tool [{tool['name']}]")
                    print(f"   Parameters: {tool['args']}\n")
            else:
                print(f"🤖 AI RESPONSE:\n{msg.content}\n")
                
        elif role == "TOOL":
            print(f"🛠️ TOOL OUTPUT (From {msg.name}):")
            content = msg.content[:300] + "..." if len(msg.content) > 300 else msg.content
            print(f"{content}\n")

    print("="*50)