import random

print("I'm thinking of a number.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while difficulty != "easy" and difficulty != "hard":
    print("Invalid.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

number = random.randint(0, 101)
low = 1
high = 100

while attempts > 0:
    print()
    print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"Range: {low} to {high}.")
    guess = int(input("Make a guess: "))
    while guess < 1 or guess > 100:
        print("Invalid.")
        guess = int(input("Make a guess: "))
    
    if guess == number:
        print(f"\nYou got it! The answer was {number}.")
        break
    else:
        if guess > number:
            print("Too high.", end=" ")
            if guess < high: high = guess
        else:
            print("Too low.", end=" ")
            if guess > low: low = guess
        print("Guess again.")
    
    attempts -= 1

if attempts == 0:
    print(f"\nYou've run out of attempts! The answer was {number}.")
    