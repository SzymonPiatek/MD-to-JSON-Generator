import random
import json
import os 
from directories import *

def open_json_file(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)

        for file in files:
            input_file_path = os.path.join(file_path, file)
            with open(input_file_path, 'r') as f:
                data = json.load(f)
                return data

def generate_phone_number():
    number = random.choices('0123456789', k=9)
    number = ''.join(map(str, number))
    if number[0] == 0:
        generate_phone_number()
    else:
        if len(number) != 9:
            generate_phone_number()
        else:
            number = str(number)
            if number in open_json_file(json_output_path):
                generate_phone_number()
            return number