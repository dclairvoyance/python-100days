# notes: try-except

import random

moves = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock, Paper, Scissors.")
while True:
    try:
        move = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        while move < 0 or move > 2:
            print("0, 1, or 2 only.")
            move = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        break
    except ValueError:
        print("Please enter int only.")

bot_move = random.randint(0, 2)

# 0 = rock
# 1 = paper
# 2 = scissors
print(f"Your move: {moves[move]}")
print(f"Bot move: {moves[bot_move]}")

if (move == bot_move):
    print("Draw")
elif (move == 0 and bot_move == 1 or \
      move == 1 and bot_move == 2 or \
      move == 2 and bot_move == 0):
    print("You lose")
else:
    print("You win")