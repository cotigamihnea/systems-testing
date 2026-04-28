import datetime
from unittest.mock import Mock

def is_leap_year():
    today = datetime.datetime.today()
    return (today.year % 4 == 0 and today.year % 100 != 0) or (today.year % 400 == 0)

an_bisect = datetime.datetime(year=2024, month=1, day=1)
an_normal = datetime.datetime(year=2023, month=1, day=1)

mock_datetime = Mock()

globals()['datetime'] = mock_datetime

mock_datetime.datetime.today.return_value = an_bisect
assert is_leap_year() == True
print("Test 1 (An bisect) a trecut!")

mock_datetime.datetime.today.return_value = an_normal
assert is_leap_year() == False
print("Test 2 (An normal) a trecut!")