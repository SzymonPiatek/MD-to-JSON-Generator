import random
from directories import *
from json_methods import open_json_file

def generate_phone_number():
    first_number = ''.join(random.choices('123456789'))
    past_numbers = ''.join(random.choices('0123456789', k=8))
    number = first_number + past_numbers
    if number[0] == '0':
        generate_phone_number()
    else:
        if len(number) != 9:
            generate_phone_number()
        else:
            number = str(number)
            if number in open_json_file(json_output_path):
                generate_phone_number()
            return number