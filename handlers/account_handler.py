from database.user_handler import insert_user, find_user_by_name, update_user, delete_user
from utils.user_info_parser import extract_user_info, check_missing_info, extract_fields

# Create a new account

def create_account(user_info):
    user_id = insert_user(user_info)
    return f"Account created for {user_info['first_name']} {user_info['last_name']}, age {user_info['age']}. User ID: {user_id}"

def create_account_tool(user_message):
    print(f"user message : {user_message}")
    user_info = extract_fields(user_message)
    print(f"user info : {user_info}")
    if not user_info:
        return "Sorry, I couldn't understand the information provided. Please try again."
    if (check_missing_info(user_info)):
        missing_fields_formatted = '\n- '.join(check_missing_info(user_info))
        print (f"Bot: I still need the following information to create your account:\n- {missing_fields_formatted}.\n Please provide it.")
    create_account(user_info)
    
# Delete User Account
def delete_account(user_message):
    user_info = extract_user_info(user_message)
    print(user_info)
    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    deleted_count = delete_user(first_name, last_name)
    if deleted_count > 0:
        return "User deleted successfully."
    else:
        return "User not found."
    

# Read User's Credentials
def read_account(user_message):
    user_info = extract_user_info(user_message)
    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    
    user = find_user_by_name(first_name, last_name)
    if user:
        return f"User found: Name: {user['first_name']} {user['last_name']}, Gender: {user['gender']}"
    else:
        return "User not found."

# Upadte User's Credentials
def update_account(user_message, update_message):
    name = extract_user_info(user_message)
    first_name = name.get('first_name')
    last_name = name.get('last_name')
    update_fields = extract_user_info(update_message)
    modified_count = update_user(first_name, last_name, update_fields)
    if modified_count > 0:
        return "User updated successfully."
    else:
        return "User not found or no changes made."
