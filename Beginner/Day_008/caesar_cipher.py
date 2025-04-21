from logo import logo

# Caesar Cipher Project
# The Caesar Cipher is one of the earliest and simplest methods of encryption technique.
# It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet.

# For example with a shift of 1, A would be replaced by B, B would become C, and so on.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# The number of positions down the alphabet is called the "shift".
# For example, with a shift of 1, A would be replaced by B, B would become C, and so on.
def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in plain_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_letter = alphabet[(position + shift_amount) % len(alphabet)]
            cipher_text += new_letter
        else:
            cipher_text += character
    print(f"The {cipher_direction}d text is {cipher_text}")

print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = None
    while shift is None:
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Please enter a valid number")
    caesar(text, shift, direction)

    reply = input("Do you what to continue?\nType 'Yes' or 'No'\n").lower()
    if reply == "no":
        should_continue = False
        print("Goodbye")
