import json
import os
from directories import *

def calculate_edited_data(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)
        edited_value = 0
        values = 0
        result = []
        print('')
        for file in files:
            input_file_path = os.path.join(file_path, file)
            file_name = os.path.splitext(file)[0]
            with open(input_file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    if value == '':
                        pass
                    else:
                        edited_value += 1
                    values += 1
                ratio = round((edited_value/values)*100, 2)
            result.append(ratio)
            print(f'{file_name}: {ratio}% edited data [{edited_value}/{values}]')
            values = 0
            edited_value = 0
    return result

def all_data_ratio(results):
    edited = 0
    all = 0
    for result in results:
        edited += result
        all += 100
    final = round((edited/all)*100, 2)
    print('')
    print(f'Program przekształcił średnio {final}% danych')

def calculate_data_print():
    all_data_ratio(calculate_edited_data(json_output_path))

