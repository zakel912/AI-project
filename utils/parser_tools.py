# Check that all essential information has been given
def check_missing_info(required_fields, user_info):
    missing_fields = []
    for field in required_fields :
        if field in user_info :
            if len(user_info[field]) == 0 or user_info[field] == "Unknown" :
                missing_fields.append(field)
        else :
            missing_fields.append(field)
    return missing_fields

def creation_check_missing_info(user_info):
    required_fields = ['first_name', 'last_name', 'gender', 'email', 'password']
    check_missing_info(required_fields, user_info)

def deletion_check_missing_info(user_info):
    required_fields = ['first_name', 'last_name', 'password']
    check_missing_info(required_fields, user_info)

def update_check_missing_info(user_info):
    required_fields = ['email', 'password']
    check_missing_info(required_fields, user_info)


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
        elif 'password' in line.lower():
            user_info['password'] = line.split(':')[-1].strip()
        elif 'email' in line.lower():
            user_info['email'] = line.split(':')[-1].strip()
        elif 'phone' in line.lower():
            user_info['phone'] = line.split(':')[-1].strip()
        elif 'gender' in line.lower():
            user_info['gender'] = line.split(':')[-1].strip().lower()
    return user_info