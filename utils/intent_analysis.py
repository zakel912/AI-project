# Import all the necessary modules
from utils.common_imports import *

# Prompt model allowing the agent to guess the user's intention
prompt_template_intent = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "Determine the intent from this message: {message}")
])

# Determine the intent of the given message using the chat model and prompt template.
def get_intent(message):
    formatted_prompt = prompt_template_intent.format_prompt(message=message)
    intent = chat_model.invoke(formatted_prompt)
    return intent.content