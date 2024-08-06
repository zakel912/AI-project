from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(model, get_session_history)

# How to use it 
# with_message_history = RunnableWithMessageHistory(chain, get_session_history)
# config = {"configurable": {"session_id": "abc2"}}

# response = with_message_history.invoke(
#     [HumanMessage(content="Hi! I'm Bob")],
#     config=config,
# )

# response.content