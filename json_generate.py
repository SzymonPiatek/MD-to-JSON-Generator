import markdown
import re
import json
from collections import OrderedDict
import os

def extract_variables_from_markdown(md_file_dir, json_file_dir):
    if os.path.exists(md_file_dir):
        files = os.listdir(md_file_dir)

        for file in files:
            file_path = os.path.join(md_file_dir, file)
            file_name = os.path.splitext(file)[0]
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            html_content = markdown.markdown(content)
            pattern = re.compile(r'\b([a-zA-Z]+_[a-zA-Z]+[a-zA-Z0-9_]*)\b')
            matches = re.findall(pattern, html_content)

            unique_variables = list(OrderedDict.fromkeys((matches)))
            json_data = {variable: 0 for variable in unique_variables}

            file_output_path = f'{json_file_dir}/{file_name}.json'
            with open(file_output_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=2)
    else:
        print('Dodaj plik .md')
        