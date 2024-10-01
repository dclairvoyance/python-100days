import random
from game_data import data

score = 0
active = True

while active:
    data_a = random.choice(data)
    data_b = random.choice(data)
    while data_a == data_b:
        data_b = random.choice(data)

    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
    print("vs")
    print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess != "a" and guess != "b":
        print("Invalid.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if data_a["follower_count"] > data_b["follower_count"]:
        correct = "a"
    elif data_a["follower_count"] < data_b["follower_count"]:
        correct = "b"
    else:
        correct = "x"

    if guess == correct or correct == "x":
        print(f"You're right. Current score: {score}.")
        score += 1
        print()
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        active = False