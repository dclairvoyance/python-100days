def caesar(text, shift, key):
    if key == "decode":
        shift *= -1
    output = ""
    for char in text:
        if char.isalpha():
            output += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            output += char
    return output  

active = True

while active:
    key = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    while key.lower() != "encode" and key.lower() != "decode":
        print("Invalid.")
        key = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    text = input("Type your message: ").lower()

    while True:
        try:
            shift = int(input("Type the shift number: "))
            break
        except ValueError:
            print("Please enter int only.")

    if key == "encode":
        encoded = caesar(text, shift, key)
        print("Here's the encoded result: %s" % encoded)
    else:
        decoded = caesar(text, shift, key)
        print("Here's the decoded result: %s" % decoded)
    
    again = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
    while again != "yes" and again != "no":
        print("Invalid.")
        again = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
    active = True if again == "yes" else False

print("Goodbye!")