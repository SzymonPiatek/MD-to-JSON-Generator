import json
import os
import random
from data_var import *
from generators.isan_generator import generate_isan
from generators.date_generator import generate_random_date
from generators.phone_number_generator import generate_phone_number
from generators.zipcode_generator import generate_zipcode
from generators.email_generator import generate_email

def remake_json(data):
    i_first_name = 0
    i_surname = 0
    i_sex = 0
    i_post_office = 0
    i_location = 0
    for key in data:
        if 'first_name' in key:
            data[key] = FIRST_NAME[i_first_name]
            if i_first_name == (len(FIRST_NAME)-1):
                i_first_name = 0
            else:
                i_first_name += 1

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
            data[key] = generate_random_date()
        
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
        
        elif 'zipcode' in key:
            data[key] = generate_zipcode()
        
        elif 'fullname' in key:
            data[key] = f'{FIRST_NAME[i_first_name]} {SURNAME[i_surname]}'
            if i_surname == (len(SURNAME)-1):
                i_surname = 0
            else:
                i_surname += 1

            if i_first_name == (len(FIRST_NAME)-1):
                i_first_name = 0
            else:
                i_first_name += 1

        elif 'is_' in key:
            data[key] = random.choice([True, False])

        elif 'post_office' in key:
            data[key] = POST_OFFICE[i_post_office]
            if i_post_office == (len(POST_OFFICE)-1):
                i_post_office = 0
            else:
                i_post_office += 1

        elif 'location' in key:
            data[key] = LOCATION[i_location]
            if i_location == (len(LOCATION)-1):
                i_location = 0
            else:
                i_location += 1

        elif 'email' in key:
            num = random.randint(0, len(CORP_NAME)-1)
            corp_name = CORP_NAME[num]
            data[key] = generate_email(corp_name)
            CORP_NAME.pop(num)

        else:
            continue

    return data

def open_json_file(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)

        for file in files:
            input_file_path = os.path.join(file_path, file)
            file_name = os.path.splitext(file)[0]
            with open(input_file_path, 'r') as f:
                data = json.load(f)
                return {'data': data, "file_name": file_name}
            
def save_json_file(file_path, file_name, data):
    file_output_path = f'{file_path}/{file_name}.json'

    with open(file_output_path, 'w') as d:
        json.dump(data, d, indent=2)

def json_remake_data(file_path):
    data, file_name = open_json_file(file_path)['data'], open_json_file(file_path)['file_name']
    rj_data = remake_json(data)
    save_json_file(file_path, file_name, rj_data)