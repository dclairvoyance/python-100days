# notes: use datatype string("__a_") or set

import nltk
import random
import string
from nltk.corpus import words

def download_words():
    try:
        words.words()
    except LookupError:
        nltk.download("words")

def display_status():
    print()
    print("Life: %d" % life)
    print("Word to guess: ", end="")
    for letter in word:
        if (letter_dict[letter] == 1):
            print(letter, end="")
        else:
            print("_", end="")
    print()

download_words()

word_list = [word for word in words.words() if len(word) >= 3 and len(word) <= 5]
word = random.choice(word_list).lower()
letter_dict = dict.fromkeys(string.ascii_lowercase, 0)
life = 6

display_status()

while life > 0:
    guess = input("Guess a letter: ").lower()

    # valid guess
    if len(guess) == 1 and guess.isalpha() and letter_dict[guess] == 0:
        
        # correct guess
        if guess in word:
            letter_dict[guess] = 1
            if all(letter_dict[letter] == 1 for letter in word):
                print("You guessed the word. You win!")
                break
        # incorrect guess
        else:
            print("You guessed %c, that's not in the word. You lose a life!" % guess)
            letter_dict[guess] = 2
            life -= 1
    # invalid guess
    else:
        print("Invalid.")

    display_status()

print("The word is %s." % word)