active = True
bids = {}

while active:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    
    more = input("Are there any other bidders? Type 'yes' or 'no': ")
    while (more != "yes" and more != "no"):
        print("Invalid.")
        more = input("Are there any other bidders? Type 'yes' or 'no': ")
    active = True if more == "yes" else False

print("The winner is %s with a bid of $%d." % (max(bids, key=bids.get), bids[max(bids, key=bids.get)]))