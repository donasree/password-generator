import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a secure password with given constraints."""
    character_pool = ""
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character set selected!"

    return ''.join(random.choice(character_pool) for _ in range(length))

# User input with validation
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Error: Length must be a positive number!")
            continue
        break
    except ValueError:
        print("Error: Please enter a valid integer for length!")

use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

password = generate_password(length, use_upper, use_lower, use_digits, use_special)
print("Generated Password:", password)
