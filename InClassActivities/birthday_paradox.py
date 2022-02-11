"""
This program will run 100,000 simulations of generating a number of random birthdays that the user inputs.
It will calculate a percentage of the simulations in which there was a matching birthday in the list of random
birthdays generated.
"""

from datetime import date, timedelta
import random


def get_random_birthdays(num_birthdays):
    birthdays = []
    for i in range(num_birthdays):
        random_birthday = date(2022, 1, 1) + timedelta(days=random.randint(1, 364))
        birthdays.append(random_birthday.strftime("%B %d"))
    return birthdays


def check_for_match(birthdays):
    for i in range(len(birthdays)):
        if birthdays.count(birthdays[i]) > 1:
            return birthdays[i]
    return None


number_of_birthdays = int(input("How many birthdays do you want for your simulation: "))
count = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations have run")
    birthday_list = get_random_birthdays(number_of_birthdays)
    if check_for_match(birthday_list):
        count = count + 1

print(count/100_000*100, "% of the simulations of", number_of_birthdays, "birthdays had a match!")
