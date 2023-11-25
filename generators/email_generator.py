import random
from data_var import EMAIL_HOST

def generate_email(name):
    email_host = EMAIL_HOST
    first_name = name.split()[0]
    email = f'{first_name.lower()}.@{random.choice(email_host)}'
    return email