import random

def generate_zipcode():
    zipcode = f'{random.randint(00, 99)}-{random.randint(100, 999)}'
    if len(zipcode) == 5:
        zipcode = '0'+ zipcode
    return zipcode