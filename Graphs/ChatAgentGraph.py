from IPython import display
from langgraph.graph import StateGraph, END ,START
from Schemas import State
from Tools import Tools
from langchain_core.messages import SystemMessage, HumanMessage
from LLMEngein import LLMProvidorFactory
from dotenv import load_dotenv
import os
load_dotenv()
from langgraph.prebuilt import ToolNode
# from langgraph.prebuilt.tool_node import tool_condition
from IPython.display import display, Image
from IPython.display import display, Markdown



tools = Tools().GetTools()
Providor = LLMProvidorFactory(llmProvidorName=os.getenv("PROVIDOR").strip().upper())
llm_engin=Providor.GetLLMProvidor()
llm_with_tools = llm_engin.bind_tools(tools)
def LLMToolCalling(state:State):
    messages = state["messages"] 
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

class ChatAgentGraph():
    def __init__(self):
        builder = StateGraph(State)

        builder.add_node("LLMToolCalling", LLMToolCalling)
        builder.add_node("Tools", ToolNode(tools)) 

        builder.add_edge(START, "LLMToolCalling")
        builder.add_edge("Tools", "LLMToolCalling")

        builder.add_conditional_edges(
            "LLMToolCalling",
            lambda state: "Tools" if state["messages"][-1].tool_calls else END
        )
        
        self.graph = builder.compile() 

    def Run(self, query: str):
        return self.graph.run(query)