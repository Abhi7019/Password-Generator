import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    password_length = int(input("Enter the desired length for the password: "))
    if password_length > 0:
        # Generate and display the password
        generated_password = generate_password(password_length)
        print("Generated Password: ", generated_password)
    else:
        print("Please enter a valid positive length for the password.")
except ValueError:
    print("Invalid input. Please enter a valid numerical value for the password length.")