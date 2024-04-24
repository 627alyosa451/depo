import random
import string

def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

length = int(input("Enter the length of your password: "))

if length < 8:
    print("Password is too short! It should be at least 8 characters long.")
else:
    password = generate_strong_password(length)
    print("Generated strong password:", password)

