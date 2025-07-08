# passwordgen.py

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
