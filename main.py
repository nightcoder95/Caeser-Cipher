# This program is to encode and decode a given input using a method called Caesar Cipher. It is mainly by shifting the character by a given amount.

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(text, shift, method):
    new_text = ""
    # Loop through each letter in textInput
    for char in text:
        if char in alphabet:
            # find the position of each letter in alphabet list through index function
            position = alphabet.index(char)
            if method == "encode":
                # add the shift amount which user entered with the current index of the letter
                new_position = alphabet[position + shift]
                # add the new letter to the new_text variable
                new_text += new_position
            elif method == "decode":
                new_position = alphabet[position - shift]
                new_text += new_position
        # if char is not present in the alphabet list eg- symbols, spaces etc, itll add to the new_text variable without adding the shift amount
        else:
            new_text += char

    print(new_text)


# Collect the data from the user
# a default boolean value is created to loop until the user want to exit from the program
flag = True
while flag:
    methodInput = input("Do you want to encode or decode?\n").lower()
    textInput = input(f"Enter the data you want to {methodInput}d: ").lower()
    shiftInput = int(input("Enter the shift amount"))
    # if the user enter shift amount which is greater than 26, there will be index error. TO avoid that, the remainder is taken and added as the shift amount
    shiftInput = shiftInput % 26
    caesar(text=textInput, shift=shiftInput, method=methodInput)
    should_continue = input("Do you wish to continue, type 'Yes'. Type 'No' to exit: ").lower()
    if should_continue == "no":
        flag = False
        print("Thank You")
