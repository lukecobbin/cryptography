#! /usr/bin/ python3

import sys

# Takes imput from the commandline and prints all 26 versions of the Caesar cipher
# Usage: python3 caesar.py JxyiyiXemJeKiuYj

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            # Apply the shift and handle wrap-around
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            # Preserve non-alphabetic characters
            result += char
    return result

def solve_caesar_cipher(ciphertext):
        for shift in range(26):
            decrypted_text = caesar_cipher(ciphertext, -shift)
            print(f"{shift:2}: {decrypted_text}")


ciphertext = sys.argv[1]
solve_caesar_cipher(ciphertext)
