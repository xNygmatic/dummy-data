from dummydata import generate_person, log_person
import random
import csv
import os


def serialize(people):
    serialized = []
    for p in people:
        serialized.append(list(p))
    return serialized


def write_csv(file_name, header, data):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar="'")
        writer.writerow(header)
        writer.writerows(data)
        csvfile.close()


def create_people(qty):
    people = []
    for idx in range(qty):
        people.append(generate_person(random.choice(["MALE", "FEMALE"]), 0))
        print(f"dummydata.py > {idx + 1} of {qty} people generated")
    print("dummydata.py > Generation Complete! Serializing data")
    header = ["FIRSTNAME", "LASTNAME", "TITLE", "AGE", "USERNAME", "EMAIL", "PASSWORD", "ADDRESS", "NUMBER", "COLOR"]
    path = os.path.dirname(os.path.realpath(__file__)) + "\\people.csv"
    write_csv(path, header, serialize(people))


if __name__ == "__main__":
    amount = 10000
    if not os.path.isfile("people.csv"):
        create_people(amount)
    else:
        for x in range(amount):
            log_person(generate_person(random.choice(["MALE", "FEMALE"]), random.randrange(17, 70)))
