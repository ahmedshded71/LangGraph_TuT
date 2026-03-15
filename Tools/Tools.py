from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
import os
load_dotenv()
from Schemas import State

class Tools():

    tavily_search = TavilySearchResults(
        max_results=3,
        tavily_api_key=os.getenv("TAVILT_API_KEY")
    ) 

    arxiv_search = ArxivQueryRun(
        api_wrapper=ArxivAPIWrapper(
            top_k_results=3,
            doc_content_chars_max=500,
        )
    )

    wikipedia_search = WikipediaQueryRun(
        api_wrapper=WikipediaAPIWrapper(
            top_k_results=3,
            doc_content_chars_max=500,
        )
    )

    tools = [tavily_search, arxiv_search, wikipedia_search]


    @classmethod
    def GetTools(cls):
        return cls.tools