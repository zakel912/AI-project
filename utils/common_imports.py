import openai
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=50,  openai_api_key=OPENAI_API_KEY)