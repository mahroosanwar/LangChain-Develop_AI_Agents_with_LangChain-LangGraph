# Implement our LangGraph nodes
from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can answer questions."""


def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """Run agent resoning node."""
    response = llm.invoke(
        [{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]]
    )  # So in the first iteration, we're going to have only the human message. In the second iteration, we're going to have also the human message and the response and so on

    return {"messages": [response]}

tool_node = ToolNode(tools)