from json_generate import extract_variables_from_markdown
from json_data_remake import json_remake_data
from directories import *


extract_variables_from_markdown(md_file_path, json_output_path)
json_remake_data(json_output_path)
