# PASSWORD GENERATOR
import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = letters + digits + special_chars

    if len(all_chars) == 0:
        print("Error: No characters selected for password generation.")
        return None

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Get user preferences
length = int(input("Enter password length: "))
use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

# Generate and print password
password = generate_password(length, use_digits, use_special_chars)
print(f"Generated Password: {password}")
