import random

def check_status(my_cards, dealer_cards):
    if (sum(my_cards) > 21):
        print("\nYou went over. You lose.")
    elif (sum(dealer_cards) > 21):
        print("\nDealer went over. You win.")
    elif (sum(my_cards) > sum(dealer_cards)):
        print("\nYou win.")
    elif (sum(my_cards) < sum(dealer_cards)):
        print("\nYou lose.")
    else:
        print("\nIt's a draw.")

again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while again != "y" and again != "n":
    print("Invalid.")
    again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
active = True if again == "y" else False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
dealer_cards = []

while active:
    # player takes a card
    my_cards.append(random.choice(cards))
    cards.remove(my_cards[0])
    # dealer takes a card
    dealer_cards.append(random.choice(cards))
    cards.remove(dealer_cards[0])
    # player takes another card
    my_cards.append(random.choice(cards))
    cards.remove(my_cards[1])
    # dealer takes another card
    dealer_cards.append(random.choice(cards))
    cards.remove(dealer_cards[1])

    print(f"\nYour hand: {my_cards}, current score: {sum(my_cards)}")
    print(f"Dealer's hand: [{dealer_cards[0]}, ?]")
    again = "y"

    while again == "y":
        if (sum(my_cards) > 21):
            print("\nYou went over. You lose.")
            print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            again = "n"
            break
        elif (sum(my_cards) == 21):
            print("\nYou have Blackjack. You win.")
            print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            again = "n"
        else:
            again = input("Type 'y' to get another card, type 'n' to pass: ")
            while again != "y" and again != "n":
                print("Invalid.")
                again = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if again == "n":
                while (sum(dealer_cards) < 17):
                    dealer_cards.append(random.choice(cards))
                    cards.remove(dealer_cards[-1])
                    if (sum(dealer_cards) > 21 and 11 in dealer_cards):
                        dealer_cards.remove(11)
                        dealer_cards.append(1)
                check_status(my_cards, dealer_cards)
                print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
                print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            else:
                my_cards.append(random.choice(cards))
                cards.remove(my_cards[-1])
                if (sum(my_cards) > 21 and 11 in my_cards):
                    my_cards.remove(11)
                    my_cards.append(1)
                print(f"\nYour hand: {my_cards}, current score: {sum(my_cards)}")
                print(f"Dealer's hand: [{dealer_cards[0]}, ?]")
    
    print()
    again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while again != "y" and again != "n":
        print("Invalid.")
        print()
        again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    active = True if again == "y" else False

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = []
    dealer_cards = []
