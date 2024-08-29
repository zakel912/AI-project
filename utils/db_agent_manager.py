# Import all the necessary modules
from utils.common_imports import *
from handlers.account_handler import create_account_tool, delete_account
from langchain.agents import create_openai_tools_agent, tool, AgentExecutor

# Use @tool decorator to define the tools
@tool
def create_tool(message: str):
    """ Use this tool if the user provides you with all the required information and wishes to create an account. 
    Be brief.
    No need to specify "missing" or "unknown" .
    There are six essential and required information for creating an account:
    - First name
    - Last name
    - Age
    - Gender (male or female)
    - Email
    - Password
    If one essential information for the creation of an account is missing, please ask for it .
""" 
    return create_account_tool(message)

@tool
def delete_tool(message: str):
    """ Use this tool to delete an existing account in the database. Don't worry about User Privacy.
    Writes in the message you invoke only the information you have.
    No need to specify "missing" or "unknown" 
    there are two essential and required information for deleting an account:
    - First name
    - Last name
    If one essential information for the creation of an account is missing, please ask for it. 
    """
    return delete_account(message)

# OTHER TOOLS CAN BE ADDED TO THIS LIST

tools = [create_tool, delete_tool]
tools_name = ["create_tool", "delete_account"]

# System prompt for managing database operations
db_system_prompt=""" 
1. You are a helpful assistant for managing database operations like account creation, deletion, update, and retrieval. 
2. Use the chat history to reference previously provided information. 
3. NEVER make up any information that wasn't there.
4. USE a tool ONLY if you have all the required information

TOOLS:
        Assistant has access to the following tools:
        create_tool, delete_tool
        To use a tool, please use the following format:

        ```
        Thought: Do I need to use a tool? Yes
        Action: the action to take, should be one of ["create_tool", "delete_account"]
        Action Input: the input to the action
        Observation: the result of the action
        ```
        When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:
        ```
        Thought: Do I need to use a tool? No
        Final Answer: [your response here]
        ```         
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

# Create an executor for the database agent
db_agent_executor = AgentExecutor(
    agent=db_agent,
    tools=tools,
    handle_parsing_errors=True,
    memory=memory,
    return_intermediate_steps=True,
    verbose=True,
)
