from wonderwords import RandomWord
from faker import Faker
import random


def generate_random_username():
    adjective = RandomWord().word(include_parts_of_speech=["adjectives"], word_max_length=8)
    noun = RandomWord().word(include_parts_of_speech=["nouns"], word_max_length=8)
    if random.choice(["SEPARATE", "COMBINE"]) == "COMBINE":
        username = f"{adjective}{noun.capitalize()}"
    else:
        separators = ["_", "-", "."]
        username = f"{adjective}{random.choice(separators)}{noun}"
    if random.choice([True, False]):
        username = f"{username}{random.randrange(0, 150)}"
    return username


def generate_username(firstname, lastname):
    manipulation_type = random.choice(["SUB", "COMBINE", "REVERSE"])
    if manipulation_type == "SUB":
        username = f"{firstname.lower()[0]} {lastname.lower()}"
    elif manipulation_type == "COMBINE":
        username = f"{firstname.lower()} {lastname.lower()}"
    else:
        username = f"{lastname.lower()} {firstname.lower()}"
    if random.choice(["SEPARATE", "COMBINE"]) == "SEPARATE":
        separators = ["_", "-", "."]
        username = username.replace(" ", random.choice(separators))
    else:
        username = username.replace(" ", "")
    if random.choice([True, False]):
        username = f"{username}{random.randrange(0, 150)}"
    return username


def generate_email(username):
    extensions = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@live.com"]
    if any(char.isdigit() for char in username):
        return f"{username}{random.choice(extensions)}"
    else:
        if random.choice([True, False]):
            username = f"{username}{random.randrange(1, 15)}"
        return f"{username}{random.choice(extensions)}"


def generate_person(gender, age):
    fake = Faker()
    if gender == "MALE":
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        title = fake.prefix_male()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        title = fake.prefix_female()
    if age == 0:
        age = random.randrange(18, 70)
    if age <= 45:
        password = fake.password(length=random.randrange(7, 12))
        user = generate_random_username()
    else:
        password = f"{last_name}{random.randrange(5, 150)}{random.choice(['$', '!', '?'])}"
        user = generate_username(first_name, last_name)
    email = generate_email(user)
    address = fake.street_address()
    number = random.randrange(1, 69)
    color = fake.color_name()
    return Person(gender, first_name, last_name, title, age, user, email, password, address, number, color)


def log_person(person):
    print(f"------------------------------------\n"
          f"Person: {person.get_title()} {person.get_firstname()} {person.get_lastname()}\n\t"
          f"Age: {person.get_age()}\n\tGender: {person.get_gender()}\n\tUsername: {person.get_username()}\n\t"
          f"Email: {person.get_email()}\n\tPassword: {person.get_password()}\n\tAddress: {person.get_address()}\n\t"
          f"Favorite Number: {person.get_favorite_number()}\n\tFavorite Color: {person.get_favorite_color()}")


class Person:
    def __init__(self, gender, firstname, lastname, title, age, username, email, password, address, number, color):
        self._favorite_color = f"\"{color}\""
        self._firstname = f"\"{firstname}\""
        self._lastname = f"\"{lastname}\""
        self._username = f"\"{username}\""
        self._password = f"\"{password}\""
        self._address = f"\"{address}\""
        self._title = f"\"{title}\""
        self._email = f"\"{email}\""
        self._favorite_number = number
        self._gender = gender
        self._age = age

    def __iter__(self):
        return iter([self._firstname, self._lastname, self._title, self._age, self._username, self._email,
                     self._password, self._address, self._favorite_number, self._favorite_color])

    def get_gender(self):
        return self._gender

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_title(self):
        return self._title

    def get_age(self):
        return self._age

    def get_username(self):
        return self._username

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_address(self):
        return self._address

    def get_favorite_number(self):
        return self._favorite_number

    def get_favorite_color(self):
        return self._favorite_color
