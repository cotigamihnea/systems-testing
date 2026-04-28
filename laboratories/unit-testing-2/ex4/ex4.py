#TODO Creati o baza de date fake ce contine minim 500 de intrari. 
# O intrare este reprezentata de o instanta a clasei Person (pe care trebuie sa o creati) 
# care are minim 3 atribute (nume, varsta, email). Cheia unica este representata de adresa de mail. 
# EXERCIȚIUL 4
from faker import Faker

class Person:
    def __init__(self, nume, varsta, email):
        self.nume = nume
        self.varsta = varsta
        self.email = email

faker = Faker()
fake_db = {}

for _ in range(500):
    email_generat = faker.unique.email()
    persoana = Person(
        nume=faker.name(),
        varsta=faker.random_int(min=18, max=90),
        email=email_generat
    )
    fake_db[email_generat] = persoana
    
    import unittest
from unittest.mock import patch
from ex3 import calculate_total 

class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        with patch('ex3.read') as mock_read:
            mock_read.return_value = [10.5, 20.0, 5.5]
            result = calculate_total('dummy.txt')
            self.assertEqual(result, 36.0)
            mock_read.assert_called_once_with('dummy.txt')

if __name__ == '__main__':
    unittest.main()