import random
from datetime import datetime, timedelta

def generate_random_date():
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 11, 25)

    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_date = start_date + timedelta(days=random_days)
    random_date = random_date.strftime('%d.%m.%Y')
    random_date = str(random_date)
    return random_date
