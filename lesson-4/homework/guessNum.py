import random

number = random.randint(1, 100)
attempts = 10
    
while attempts:
    guess = int(input("Guess a number: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
    attempts -= 1
    
if attempts == 0:
    print("You lost")
#/