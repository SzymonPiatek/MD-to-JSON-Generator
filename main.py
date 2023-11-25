from json_generate import extract_variables_from_markdown
from json_data_remake import open_json_file
from directories import *


extract_variables_from_markdown(md_file_path, json_output_path)
open_json_file(json_output_path)
