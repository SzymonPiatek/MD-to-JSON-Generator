import random

def generate_nip():
    nip = ''.join(random.choice('0123456789', k=10))
    nip = str(nip)

    if len(nip) != 10:
        generate_nip()

    return nip