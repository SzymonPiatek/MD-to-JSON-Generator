import os
import random
from data_var import *
from generators.isan_generator import generate_isan
from generators.date_generator import generate_random_date
from generators.phone_number_generator import generate_phone_number
from generators.zipcode_generator import generate_zipcode
from generators.nip_generator import generate_nip
from json_methods import *

def remake_json(data):
    i_first_name = 0
    i_surname = 0
    i_sex = 0
    i_post_office = 0
    i_location = 0
    i_corp_name_name = 0
    i_house_num = 0
    i_apartment_num = 0
    i_municipality = 0
    i_county = 0
    i_voivodeship = 0
    for key in data:
        # Personal data
        if 'name' in key:
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

            else:
                data[key] = CORP_NAME[i_corp_name_name]
                if i_corp_name_name == (len(CORP_NAME)-1):
                    i_corp_name_name = 0
                else:
                    i_corp_name_name += 1

        elif 'sex' in key:
            data[key] = SEX[i_sex]
            if i_sex == (len(SEX)-1):
                i_sex = 0
            else:
                i_sex += 1

        elif 'phone_num' in key:
            data[key] = generate_phone_number()

        elif 'position' in key:
            num = random.randint(0, len(POSITION)-1)
            data[key] = POSITION[num]
            POSITION.pop(num)

        # Location
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

        elif 'house_num' in key:
            data[key] = HOUSE_NUM[i_house_num]
            if i_house_num == (len(HOUSE_NUM)-1):
                i_house_num = 0
            else:
                i_house_num += 1

        elif 'apartment_num' in key:
            data[key] = APARTMENT_NUM[i_apartment_num]
            if i_apartment_num == (len(APARTMENT_NUM)-1):
                i_apartment_num = 0
            else:
                i_apartment_num += 1

        elif 'municipality' in key:
            data[key] = MUNICIPALITY[i_municipality]
            if i_municipality == (len(MUNICIPALITY)-1):
                i_municipality = 0
            else:
                i_municipality += 1

        elif 'county' in key:
            data[key] = COUNTY[i_county]
            if i_county == (len(COUNTY)-1):
                i_county = 0
            else:
                i_county += 1

        elif 'voivodeship' in key:
            data[key] = VOIVODESHIP[i_voivodeship]
            if i_voivodeship == (len(VOIVODESHIP)-1):
                i_voivodeship = 0
            else:
                i_voivodeship += 1

        elif 'street' in key:
            num = random.randint(0, len(STREET)-1)
            data[key] = STREET[num]
            STREET.pop(num)
        
        elif 'zipcode' in key:
            data[key] = generate_zipcode() 

        elif 'country' in key:
            data[key] = 'Polska'

        # ====== ===== ===== =====

        elif 'main_title' in key:
            data[key] = MOVIE[random.randint(1, len(MOVIE) - 1)]

        elif 'isan_edir' in key:
            data[key] = generate_isan()

        elif 'date' in key:
            data[key] = generate_random_date()
        
        elif 'nip' in key:
            data[key] = generate_nip()

        elif 'is_'in key:
            data[key] = random.choice([True, False]) 

        elif '_check' in key:
            data[key] = random.choice([True, False])

        elif '_no_' in key:
            data[key] = random.choice([True, False])

        elif '_not_present' in key:
            data[key] = random.choice([True, False]) 

        elif 'vacant' in key:
            data[key] = random.choice([True, False])

        else:
            continue

    return data

def json_remake_data(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)
        i = 0
        for _ in files:
            data = open_json_file_result(file_path)[i]['data']
            file_name = open_json_file_result(file_path)[i]['file_name']
            rj_data = remake_json(data)
            save_json_file(file_path, file_name, rj_data)
            i += 1
