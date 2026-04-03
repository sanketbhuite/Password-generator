import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4."
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

try:
    username = input("Enter username: ")
    length = int(input("Enter the desired password length: "))

    password = generate_password(length)

    print("Generated Password:", password)

    # Save to file
    with open("passwords.txt", "a") as file:
        file.write(f"Username: {username} | Password: {password}\n")

    print("Saved to passwords.txt successfully.")

except ValueError:
    print("Please enter a valid number.")
