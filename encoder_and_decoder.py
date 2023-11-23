'''
Code authors: Jeremiah E. Ochepo
Code Title: Caesar Cipher Encoder Python (Encoder)
Program Description: This program encodes a file using the Caesar cipher.
Date created: 7/15/2019
Last modified: 7/15/2019
'''

def encoder():
    file_Name = input("Please enter the file name: ")
    shift_Number = int(input("Please enter the shift value? "))

    with open(file_Name, "r") as file_opener:
        file_strings = file_opener.read()

    encodedMsg = ""

    for character in file_strings:
        if character.isalpha():
            if character.islower():
                alphabet_location = (ord(character) - ord('a') + shift_Number) % 26
                encodedMsg += chr(alphabet_location + ord('a'))
            else:
                alphabet_location = (ord(character) - ord('A') + shift_Number) % 26
                encodedMsg += chr(alphabet_location + ord('A'))
        else:
            encodedMsg += character

    print("\nOriginal message:", file_strings)
    print("\nEncoded message:", encodedMsg)
    print("\nEach alphabet shifted:", shift_Number, "times to the right")

encoder()
