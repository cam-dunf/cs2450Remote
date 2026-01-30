import random

print("I will try to guess your age!")
name = input("What's your name? ")

guesses = 0

while guesses < 5:
    age = random.randint(15, 30)
    answer = input(f"Is your age {age}? (y/n) ")

    if answer == 'y':
        print(name, "is", age, "years old.")
        break
    else:
        print("Rats.")
        guesses += 1

if guesses == 5:
    print("I give up!")
