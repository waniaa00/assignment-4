def get_user_data():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    email = input("Enter your email address: ").strip()
    
    return first_name, last_name, email 

def main():
    user_data = get_user_data()
    
    
    print(f"Received the following user data: {user_data}")

if __name__ == '__main__':
    main()