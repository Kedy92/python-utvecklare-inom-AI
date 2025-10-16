import random

def guess_number():
    # Slumpa ett tal mellan 1 och 100
    secret_number = random.randint(1, 100)
    
    guesses = []   # Lista för alla gissade tal
    attempts = 0        # Antal försök

    print("Welcome to 'Guess the Number''!")
    print("I'm thinking of a number between 1 and 100... Can you find it?")

    while True:   # fortsätt tills man gissar rätt
        try:
            guess = int(input("Write your number: "))
        except ValueError:
            print("Please enter whole numbers only.")
            continue

        guesses.append(guess)  # lägg till gissningen i listan
        attempts += 1                   # öka antalet försök

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again..")
        else:
            print(f"Right! The number was {secret_number}.")
            print(f"You did it in {attempts} attempts.")
            print(f"Your guesses: {guesses}")
            break  # avsluta loopen när man gissar rätt

# starta spelet
guess_number()

