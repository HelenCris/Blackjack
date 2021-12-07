import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

the_number = random.randint(1, 100)
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choose_difficulty == "easy": 
    print("You have 10 attempts remain  to guess the number.")
    number_attempts = 10
    play =  False
    while not play:
        number_attempts -= 1
        guess = int(input("Make a guess: "))
        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            play = True 
        elif guess > the_number:
            print("Too high")
            print("Guess again.")
            print(f"You have {number_attempts} attempts remaining to guess the number. ")
        elif guess < the_number:
            print("Too low")
            print("Guess again.")
            print(f"You have {number_attempts} attempts remaining to guess the number. ")
        elif number_attempts == 0:
            print("You've run out of guesses, you lose.")
            break
        continue
        
if choose_difficulty == "hard": 
    print("You have 5 attempts remain  to guess the number.")
    number_attempts = 5
    play =  False
    while not play:
        guess = int(input("Make a guess: "))
        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            play = True 
        elif guess > the_number:
            print("Too high")
            print("Guess again.")
            number_attempts -= 1
            print(f"You have {number_attempts} attempts remaining to guess the number. ")
        elif guess < the_number:
            print("Too low")
            print("Guess again.")
            print(f"You have {number_attempts} attempts remaining to guess the number. ")
        elif number_attempts == 0:
            print("You've run out of guesses, you lose.")
            play = True
        continue
        
