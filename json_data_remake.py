import json
import os
import random
from data_var import *
from generators.isan_generator import generate_isan
from generators.date_generator import random_date
from generators.phone_number_generator import generate_phone_number

def remake_json(data):
    i_name = 0
    i_surname = 0
    i_sex = 0
    for key in data:
        if 'first_name' in key:
            data[key] = NAME[i_name]
            if i_name == (len(NAME)-1):
                i_name = 0
            else:
                i_name += 1
                
        elif 'last_name' in key:
            data[key] = SURNAME[i_surname]
            if i_surname == (len(SURNAME)-1):
                i_surname = 0
            else:
                i_surname += 1

        elif 'sex' in key:
            data[key] = SEX[i_sex]
            if i_sex == (len(SEX)-1):
                i_sex = 0
            else:
                i_sex += 1

        elif 'main_title' in key:
            data[key] = MOVIE[random.randint(1, len(MOVIE) - 1)]

        elif 'isan_edir' in key:
            data[key] = generate_isan()

        elif 'date_created' in key:
            data[key] = random_date()
        
        elif 'phone_num' in key:
            data[key] = generate_phone_number()
        
        elif 'position' in key:
            num = random.randint(0, len(POSITION)-1)
            data[key] = POSITION[num]
            POSITION.pop(num)
        
        elif 'street' in key:
            num = random.randint(0, len(STREET)-1)
            data[key] = STREET[num]
            STREET.pop(num)
        
        else:
            continue

def open_json_file(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)

        for file in files:
            input_file_path = os.path.join(file_path, file)
            file_name = os.path.splitext(file)[0]
            with open(input_file_path, 'r') as f:
                data = json.load(f)
            
            remake_json(data)

            file_output_path = f'{file_path}/{file_name}.json'

            with open(file_output_path, 'w') as d:
                json.dump(data, d, indent=2)