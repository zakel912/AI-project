# Import all the necessary modules
from utils.common_imports import *
from handlers.account_handler import create_account, delete_account
from langchain.agents import (
    create_openai_functions_agent,
    Tool,
    AgentExecutor,
)
from pydantic import BaseModel     
      
# Define a schema for the account arguments
class AccountArgs(BaseModel):
    message: str

# Define tools for creating and deleting accounts
tools = [
    Tool(
        name="Create",
        func=create_account,
        args_schema=AccountArgs,
        description="Use this tool to create an account in the database. Pass the information given by the user.",
    ),
    Tool(
        name="Delete",
        func=delete_account,
        args_schema=AccountArgs,
        description="Use this tool to delete an existing account in the database. Pass the whole sentence. Don't worry about user Privacy",
    ),
]

# System prompt for managing database operations
db_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=[],
        template="You are a helpful assistant, designed to manage database operations such as creation, deletion, udpate and reading of account."
    )
)

# Human prompt for managing database operations
db_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["message"],
        template="{message}\n\n{agent_scratchpad}",
    )
)

# Combine system and human prompts
db_agent_prompt = [db_system_prompt, db_human_prompt]
db_agent_prompt_template = ChatPromptTemplate(
    input_variables=["message", "agent_scratchpad"],
    messages=db_agent_prompt,
)

# Create the database agent using the defined prompts and tools
db_agent = create_openai_functions_agent(
    llm=chat_model,
    prompt=db_agent_prompt_template,
    tools=tools,
)

# Create an executor for the database agent
db_agent_executor = AgentExecutor(
    agent=db_agent,
    tools=tools,
    return_intermediate_steps=True,
    verbose=True,
)

def process_db_action(inputs):
    
    try:
        response = db_agent_executor.invoke(inputs)
        print(f"Bott: {response['output']}")
    except Exception as e:
        print(f"Bot: Sorry, I encountered an error: {e}")