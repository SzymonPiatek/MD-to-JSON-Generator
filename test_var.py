from data_var import *
from generators.date_generator import *
from generators.isan_generator import *
from generators.zipcode_generator import *
from generators.email_generator  import *
from generators.phone_number_generator import *

class TestIsanGenerator:
    def test_isan_at_the_start(self):
        assert generate_isan()[0:4] == 'ISAN'
    def test_len_of_isan(self):
        assert len(generate_isan()) == 38
    def test_mid_line_amount(self):
        assert generate_isan().count("-") == 7
    def test_is_last_letter(self):
        assert generate_isan()[-1] in LETTERS

class TestPersonalData:
    def test_len_personal_data(self):
        assert len(FIRST_NAME) == len(SURNAME)
        assert len(SURNAME) == len(SEX)

class TestDateGenerator:
    def test_date_generator(self):
        assert len(generate_random_date()) == 10

class TestZipcodeGenerator:
    def test_zipcode_generator(self):
        assert len(generate_zipcode()) == 6

class TestEmailGenerator:
    def test_email_generator(self):
        emails = []
        for name in CORP_NAME:
            emails.append(generate_email(name))
        for email in emails:
            email_host = email.split('@')[1]
            assert '@' in email
            assert email_host in EMAIL_HOST

class TestPhoneNumberGenerator:
    def test_phone_number_generator(self):
        assert len(generate_phone_number()) == 9
    def test_many_phone_number(self):
        phone_book = []
        for i in range(100):
            phone_book.append(generate_phone_number())
            i += 1
        for number in phone_book:
            assert len(number) == 9
            assert number[0] != 0