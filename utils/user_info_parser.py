# Import all the necessary modules
from utils.common_imports import *

# Template prompt for extracting user information
extract_user_info_template_str = """

Extract the essential personal information of the user from this message: {message}. 

There are four essential and required information for creating an account:
- First name
- Last name
- Age
- Gender
If one essential information for the creation of an account is missing, please ask for it.

--------- Example Input ----------
User : want to create an account for mustafa benad who is a 24 yo syrian man
(This is just an example never use these information)
"""

system_template_str = """ 
####### Few Indications on how to behave #######

1. You are a helpful AI assistant for an IDEMIA platform, be polite in your greetings.
2. You are a thoroughly trained machine learning model that is an expert in managing database.
3. You never make up any information that isn't there.

"""

example_output = """ 
------- Example output -------
(This is just an example never use these information if not given by the user)
Bot : Summary of your personal information
- First name: Mustafa
- Last name: Benad
- Age: 24
- Gender : male
- Nationality: Syrian

"""

# System prompt for extracting user information
extract_user_info_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables = [],
        template = """you are a helpful AI assistant""",
    )
)

# Human prompt for extracting user information
extract_user_info_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables = ["message"],
        template = extract_user_info_template_str,
    )
)

# Human prompt for extracting user information
extract_user_info_assistant_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables = [],
        template = example_output,
    )
)

# Combine system and human prompt
messages = [extract_user_info_system_prompt, extract_user_info_human_prompt, extract_user_info_assistant_prompt]
extract_user_info_prompt_template = ChatPromptTemplate(
    input_variables = ["message"],
    messages = messages,
)

# Check that all essential information has been given
def check_missing_info(user_info):
    required_fields = ['first_name', 'last_name', 'age', 'gender']
    missing_fields = [field for field in required_fields if field not in user_info or not user_info[field]]
    return missing_fields

# Extract from the agent output all the information needed
def extract_fields(response) :
    # All the information you may need to create an account will be added here.
    user_info = {}
    for line in response.split(','):
        if 'first name' in line.lower():
            user_info['first_name'] = line.split(':')[-1].strip()
        elif 'last name' in line.lower():
            user_info['last_name'] = line.split(':')[-1].strip()
        elif 'age' in line.lower():
            user_info['age'] = line.split(':')[-1].strip()
        elif 'country' in line.lower():
            user_info['country'] = line.split(':')[-1].strip()
        elif 'email' in line.lower():
            user_info['email'] = line.split(':')[-1].strip()
        elif 'phone' in line.lower():
            user_info['phone'] = line.split(':')[-1].strip()
        elif 'gender' in line.lower():
            user_info['gender'] = line.split(':')[-1].strip().lower()
    return user_info

# Extract user information from the given message using the chat model & prompt template.
def extract_user_info(message):
    
    review_chain = extract_user_info_prompt_template | model | StrOutputParser()
    
    try:
        response = review_chain.invoke(message)
    except Exception as e:
        print(f"Error invoking model: {e}")
        return {}
    print(f"Bot : {response}")

    user_info = extract_fields(response)
    return user_info
