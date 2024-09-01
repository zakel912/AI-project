# Import all the necessary modules
from utils.common_imports import *
from handlers.account_handler import create_account_tool, delete_account_tool, update_account_tool
from langchain.agents import create_openai_tools_agent, tool, AgentExecutor

# Use @tool decorator to define the tools
@tool
def create_tool(message: str):
    """Use this tool if the user provides you with all the required information and wishes to create an account. 
    Be brief.
    Writes in the message you invoke only from the information you just have been given.
    No need to specify "missing" or "unknown" 
    There are six essential pieces of information required to creating an account:
    - First name
    - Last name
    - Age
    - Gender (male or female)
    - Email
    - Password
    If one essential information for the creation of an account is missing, please ask for it. 
""" 
    return create_account_tool(message)

@tool
def delete_tool(message: str):
    """ Use this tool if the user provides you with all the required information and wishes to delete an account.
    Don't worry about User Privacy.
    There are three essential pieces of information required to delete an account:
    - First name
    - Last name
    - Password
    If one essential information for the creation of an account is missing, please ask for it. 
    """
    return delete_account_tool(message)

@tool
def update_tool(message: str):
    """ Use this tool to update information in user account. 
    Instructions:
    1. Focus solely on the information provided by the user. Do not add or create any information not explicitly given.
    2. Don't worry about User Privacy.
    3. There are three essential pieces of information required to update an account:

   - Email
   - Password
   - The specific information to update.
    """
    return update_account_tool(message)

# OTHER TOOLS CAN BE ADDED TO THIS LIST
# List of tools
tools = [create_tool, delete_tool, update_tool]
# List of tools name
tools_name = ["create_tool", "delete_account", "update_account"]

# System prompt for managing database operations
db_system_prompt=""" 

- You are a helpful assistant for managing database operations like account creation, deletion, update, and retrieval. 
- Focus on the new message but use the chat history to reference previously provided information.  
- Never make up any information that wasn't there. Ask for information if not given by the user
- Think twice before using a tool, you need required information to use one.

"""

# Combine system and human prompts
db_agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", db_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","new message : {message}\n\n{agent_scratchpad}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

# Create the database agent using the defined prompts and tools
db_agent = create_openai_tools_agent(
    llm=model,
    prompt=db_agent_prompt,
    tools=tools,
)

# Manage Conversation History
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key='output')

# Create an executor for the database agent that can be called up later 
db_agent_executor = AgentExecutor(
    agent=db_agent,
    tools=tools,
    handle_parsing_errors=True,
    memory=memory,
    # return_intermediate_steps=True,
    # verbose=True,
)
