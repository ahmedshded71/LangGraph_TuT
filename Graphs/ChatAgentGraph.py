from IPython import display
from langgraph.graph import StateGraph, END ,START
from Schemas import State
from Tools import Tools
from LLMEngein import LLMProvidorFactory
from dotenv import load_dotenv
import os
load_dotenv()
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tool_condition
from IPython.display import display, Image


tools = Tools().GetTools()
llm = LLMProvidorFactory(llmProvidorName=os.getenv("PROVIDER")).GetLLM()
llm_with_tools = llm.bind_tools(tools)
def ToolCallingLLM(state:State):
    return {"messages": [llm_with_tools.invoke(state.messages)]}

class ChatAgentGraph():
    def __init__(self):
        self.graph = StateGraph(State)
        # build the graph
        self.graph.add_node("ToolCallingLLM", ToolCallingLLM)
        self.graph.add_edge("Tools", ToolNode(tools))
        # add conditional edges
        self.graph.add_edge(START, "ToolCallingLLM")
        self.graph.add_conditional_edges("ToolCallingLLM", tool_condition)
        self.graph.add_edge("Tools", "ToolCallingLLM")
        # compile the graph
        self.graph = self.graph.compile()
    
    def ViewGraph(self):
        return display(Image(self.graph.get_graph().draw_mermaid_png()))

    def Run(self, query: str):
        return self.graph.run(query)