# TODO Creati un stub si o functie fake care sa simuleze 
# functionalitatea metodei get(cheie_unica) pe o baza de date. 
# Puteti sa folositi baza de date creata anterior. 
# EXERCIȚIUL 5
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
def get_person(cheie_unica):
    return fake_db.get(cheie_unica, None)

cheie_test = list(fake_db.keys())[0]
persoana_gasita = get_person(cheie_test)

assert persoana_gasita is not None
assert persoana_gasita.email == cheie_test

persoana_inexistenta = get_person("email_fals@test.com")
assert persoana_inexistenta is None

def get_person(cheie_unica):
    return fake_db.get(cheie_unica, None)

print("\n--- Rulare Teste Exercițiul 5 ---")


cheie_test = list(fake_db.keys())[0]
persoana_gasita = get_person(cheie_test)

assert persoana_gasita is not None
assert persoana_gasita.email == cheie_test
print(f"TEST 1 PASSED: Am găsit cu succes persoana în DB: {persoana_gasita.nume}")

persoana_inexistenta = get_person("email_fals_complet_inventat@test.com")

assert persoana_inexistenta is None
print("TEST 2 PASSED: Sistemul a returnat corect 'None' pentru un email fals.")