#!/usr/bin/env python3

import sys
import string

def caesar_cipher(text, shift):
    result = []
    all_printable = string.printable  # Get all printable ASCII characters

    for char in text:
        if char in all_printable:
            index = all_printable.index(char)
            shifted_index = (index + shift) % len(all_printable)
            result.append(all_printable[shifted_index])
        else:
            result.append(char)

    return ''.join(result)

def main(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as file:
            text = file.read()

        ciphered_text = text
        for _ in range(shift):
            ciphered_text = caesar_cipher(ciphered_text, shift)

        with open(output_file, 'w') as file:
            file.write(ciphered_text)

        print(f"Ciphered text has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_file shift_amount")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        shift_amount = int(sys.argv[3])
        main(input_file, output_file, shift_amount)
