import random
from data_var import LETTERS

def generate_number():
    unique_number = ''.join(random.choice('012345679') for _ in range(4))
    return unique_number

def generate_str():
    unique_str = ''.join(random.choice('012345679ABCDEFGHIJK') for _ in range(4))
    return unique_str

def random_letter():
    letter = random.choice(LETTERS)
    return letter

def generate_isan(): 
    isan = f"ISAN {generate_number()}-{generate_number()}-{generate_str()}-{generate_number()}-{random_letter()}-{generate_number()}-{generate_number()}-{random_letter()}"
    return isan