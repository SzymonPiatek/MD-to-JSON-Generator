from data_var import *
from generators.date_generator import *
from generators.isan_generator import *
from generators.zipcode_generator import *

import pytest

class TestIsanGenerator:
    def test_isan_at_the_start(self):
        assert generate_isan()[0:4] == 'ISAN'
    def test_len_of_isan(self):
        assert len(generate_isan()) == 38
    def test_mid_line_amount(self):
        assert generate_isan().count("-") == 7
    def test_is_last_letter(self):
        assert generate_isan()[-1] in 'ABCDEFGHIJKMNOPQRSTUVWXYZ'

class TestPersonalData:
    def test_len_personal_data(self):
        assert len(NAME) == len(SURNAME)
        assert len(SURNAME) == len(SEX)

class TestDateGenerator:
    def test_date_generator(self):
        assert len(random_date()) == 10

class TestZipcodeGenerator:
    def test_zipcode_generator(self):
        assert len(generate_zipcode()) == 6
