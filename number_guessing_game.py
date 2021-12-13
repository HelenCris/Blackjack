import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

the_number = random.randint(1, 100)
choose_difficulty = int(input("Choose a difficulty.\n1 - Easy\n2 - Hard \nType:  "))


def level():
    if choose_difficulty == 1: 
       return 10     
    elif choose_difficulty == 2: 
        return 5 
    else:
        print("You write wrong! Try again.")

class Sorting:
    def game(turn):
        turn = level()
        print(f"You have {turn} attempts remain  to guess the number.") 
        for i in range(turn):
            guess = int(input("Make a guess: "))
            if ((turn - i) -1) == 0:
                print("You've run out of guesses, you lose.")
                break
            else:
                if guess == the_number:
                    print(f"You got it! The answer was {the_number}.")
                    break
                elif guess > the_number:
                    print("Too high")
                elif guess < the_number:
                    print("Too low") 
            print("Guess again.")
            print(f"You have {(turn - i) - 1} attempts remain  to guess the number.") 
       
Sort = Sorting()
Sort.game()

