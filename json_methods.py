import json
import os

def save_json_file(file_path, file_name, data):
    file_output_path = f'{file_path}/{file_name}.json'
    with open(file_output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

def open_json_file(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)

        for file in files:
            input_file_path = os.path.join(file_path, file)
            with open(input_file_path, 'r') as f:
                data = json.load(f)
                return data

def open_json_file_result(file_path):
    if os.path.exists(file_path):
        files = os.listdir(file_path)
        result = []
        for file in files:
            input_file_path = os.path.join(file_path, file)
            file_name = os.path.splitext(file)[0]
            with open(input_file_path, 'r') as f:
                data = json.load(f)
                result.append({'data': data, "file_name": file_name})
        return result
    