import markdown
import re
import json
from collections import OrderedDict
import os

def extract_variables_from_markdown(input_path, output_path):
    if os.path.exists(input_path):
        files = os.listdir(input_path)

        for file in files:
            file_path = os.path.join(input_path, file)
            file_name = os.path.splitext(file)[0]
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            html_content = markdown.markdown(content)
            pattern = re.compile(r'\b([a-zA-Z]+_[a-zA-Z]+[a-zA-Z0-9_]*)\b')
            matches = re.findall(pattern, html_content)

            unique_variables = list(OrderedDict.fromkeys((matches)))
            json_data = {variable: "test" for variable in unique_variables}

            file_output_path = f'{output_path}{file_name}.json'

            with open(file_output_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=2)

md_file_path = "md_input"
json_output_path = "json_output/"

extract_variables_from_markdown(md_file_path, json_output_path)



