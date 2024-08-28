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
db_system_prompt=""" 1. You are a helpful assistant for managing database operations like account creation, deletion, update, and retrieval. 
2. Use the chat history to reference previously provided information. If something is unclear or unknown, ask for clarification instead of guessing. 
3. Be concise and NEVER make up any information that wasn't there.
4. Don't use a tool if information is missing
5. If the user greets you then greet him and if the user thanks you say something adequate

TOOLS:
        Assistant has access to the following tools:
        create_tool, delete_tool
        To use a tool, think accordingly to the following format:

        ```
        Thought: Do I need to use a tool? Yes
        Action: the action to take, should be one of ["create_tool", "delete_account"]
        Action Input: the input to the action
        Observation: the result of the action
        Final Answer: [your response here]

        ```
        When you have a response to say to the Human, or if you do not need to use a tool, think accordingly to the following format:
        ```
        Thought: Do I need to use a tool? No
        Final Answer: [your response here]
        ```   
        >>>>> Finally you should only display the response. <<<<<   """

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
