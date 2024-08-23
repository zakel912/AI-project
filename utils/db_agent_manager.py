# Import all the necessary modules
from utils.common_imports import *
from handlers.account_handler import create_account, delete_account
from langchain.agents import create_openai_tools_agent, tool, AgentExecutor

# Use @tool decorator to define the tools
@tool
def create_tool(message: str):
    """ Use this tool to create an account in the database. Pass the information given by the user from the actual message and the previous one. """
    return create_account(message)

@tool
def delete_tool(message: str):
    """ Use this tool to delete an existing account in the database. Don't worry about User Privacy """
    return delete_account(message)

# OTHER TOOLS CAN BE ADDED TO THIS LIST

# System prompt for managing database operations
db_system_prompt=""" You are a helpful assistant for managing database operations like account creation, deletion, update, and retrieval. Use the chat history to reference previously provided information. If something is unclear or unknown, ask for clarification instead of guessing. Be concise and don't make up any information.
"""

# Combine system and human prompts
db_agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", db_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{message}\n\n{agent_scratchpad}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

tools = [create_tool, delete_tool]

# Create the database agent using the defined prompts and tools
db_agent = create_openai_tools_agent(
    llm=model,
    prompt=db_agent_prompt,
    tools=tools,
)

# Manage Conversation History
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key='output')

# Create an executor for the database agent
db_agent_executor = AgentExecutor(
    agent=db_agent,
    tools=tools,
    handle_parsing_errors=True,
    memory=memory,
    # return_intermediate_steps=True,
    # verbose=True,
)
