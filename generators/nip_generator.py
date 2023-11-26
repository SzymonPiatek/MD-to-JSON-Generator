import random
from directories import *
from json_methods import *

def generate_nip():
    first_number = ''.join(random.choice('123456789'))
    past_numbers = ''.join(random.choices('0123456789', k=9))
    nip = first_number + past_numbers
    if nip[0] == 0:
        generate_nip
    else:
        if len(nip) != 10:
            generate_nip()
        else:
            nip = str(nip)
            if nip in open_json_file(json_output_path):
                generate_nip()
            return nip