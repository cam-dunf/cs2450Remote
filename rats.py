import random

print("I will try to guess your age.")
name = input("What is your name? ")

while True:
    age = random.randint(15, 30)
    answer = input(f"Is your age {age}? (y/n) ")

    if answer == 'y':
        print(name, "is", age, "years old.")
        break
    else:
        print("Rats.")