import random
import faker_DATA
from datetime import date, timedelta
from transliterate import translit

def generate_full_name():
    st_name_tuple = random.choice(faker_DATA.names_with_gender)
    st_name = st_name_tuple[1]
    st_surname_tuple = random.choice(faker_DATA.surname_pairs)
    st_surname = st_surname_tuple[(st_name_tuple[0] - 1) * -1]
    st_patronymic_triple = random.choice(faker_DATA.patronymic_triples)
    st_patronymic = st_patronymic_triple[st_name_tuple[0]]
    prnt_name = st_patronymic_triple[2]
    prnt_surname = st_surname_tuple[0]
    prnt_patronymic = random.choice(faker_DATA.patronymic_triples)[1]
    return f"{st_surname} {st_name} {st_patronymic}", f"{prnt_surname} {prnt_name} {prnt_patronymic}"


def generate_phone_number():
    prefix = "+7"
    first_three = random.randint(900, 999)
    second_three = random.randint(900, 999)
    first_two = random.randint(10, 99)
    second_two = random.randint(10, 99)
    return f"{prefix} ({first_three}) {second_three}-{first_two}-{second_two}"

house_numbers = list(range(1, 50))

def generate_address():
    city = "Орёл"
    street = random.choice(faker_DATA.orlovskie_ulitsy)
    house_num = random.choice(house_numbers)
    return f"{city}, ул. {street}, д.{house_num}"


# Генерация даты рождения (случайная дата между 18 и 70 годами назад)
def generate_birth_date():
    today = date.today()
    min_age_years = 9
    max_age_years = 17

    # Выбираем случайный возраст между минимальным и максимальным возрастом
    age_in_days = random.randint(min_age_years * 365, max_age_years * 365)
    birth_date = today - timedelta(days=age_in_days)
    return birth_date.strftime('%d.%m.%Y')


def to_email(full_name):
    parts = full_name.split()  # разбиваем строку по пробелам
    surname, name, patronymic = (
        translit(parts[0], "ru", reversed=True),
        translit(parts[1], "ru", reversed=True),
        translit(parts[2], "ru", reversed=True)
    )
    email = f"{surname.lower()}_{name.lower()}_{patronymic.lower()}@it-cube.ru"
    return email.replace("'", "")

def section():
    return random.choice(faker_DATA.sections)

def state():
    return random.choice([True, False])