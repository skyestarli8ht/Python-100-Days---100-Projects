import random

secret = random.randint(1, 10)
print("****Welcome to Number Guessing Game****")
guess = int(input("Take a guess : "))
tries = 2
while tries > 0:
    if guess == secret:
        print(f"You got it!! You got {tries+1} stars.")
        break
    elif guess > secret:
        print("Uh-oh!! Wrong Guess. Lost a life.")
        print("Too high! Try again.")
    else:
        print("Uh-oh!! Wrong Guess. Lost a life.")
        print("Too low! Try again.")
    tries -= 1
    guess = int(input("Take another guess: "))
    

if tries == 0:
    print(f"You run out of lifes... The secret number was {secret}.")