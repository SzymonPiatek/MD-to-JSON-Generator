import markdown
import re
import json
from collections import OrderedDict

def extract_variables_from_markdown(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Konwertuj plik Markdown na HTML
    html_content = markdown.markdown(content)

    # Zdefiniuj wzorzec dla zmiennych zapisanych w formie test_variable_name
    pattern = re.compile(r'\b([a-zA-Z]+_[a-zA-Z]+[a-zA-Z0-9_]*)\b')

    # Znajdź wszystkie dopasowania wzorca w HTML
    matches = re.findall(pattern, html_content)

    # Wypisz unikalne zmienne
    unique_variables = list(OrderedDict.fromkeys((matches)))
    json_data = {variable: "test" for variable in unique_variables}
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=2)

md_file_path = "md/plik.md"
json_output_path = "json/plik.json"

extract_variables_from_markdown(md_file_path, json_output_path)


