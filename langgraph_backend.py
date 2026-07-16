import logging
from typing import TypedDict, Annotated

try:
    from langchain_core.messages import BaseMessage
    from langchain_openai import ChatOpenAI
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages

    llm = ChatOpenAI()

    class ChatState(TypedDict):
        messages: Annotated[list[BaseMessage], add_messages]

    def chat_node(state: ChatState):
        messages = state['messages']
        response = llm.invoke(messages)
        return {"messages": [response]}

    checkpointer = InMemorySaver()

    graph = StateGraph(ChatState)
    graph.add_node("chat_node", chat_node)
    graph.add_edge(START, "chat_node")
    graph.add_edge("chat_node", END)

    chatbot = graph.compile(checkpointer=checkpointer)
except Exception as exc:
    logging.warning("LangGraph backend unavailable, using placeholder chatbot: %s", exc)

    class DummyMessage:
        def __init__(self, content: str):
            self.content = content

    class DummyChatbot:
        def invoke(self, state, config=None):
            messages = state.get('messages', [])
            latest = messages[-1] if messages else {}
            if isinstance(latest, dict):
                user_text = latest.get('content', '')
            else:
                user_text = getattr(latest, 'content', str(latest))
            return {"messages": [DummyMessage(f"This is a placeholder response. Your input was: {user_text}")]}

    chatbot = DummyChatbot()
