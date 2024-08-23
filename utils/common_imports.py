import openai
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Initialize the ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=50,  openai_api_key=OPENAI_API_KEY)
