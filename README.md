# Coded Correspondence 
### Overview

This project implements classical substitution ciphers in Python as part of the Codecademy Learn Python 3 – Off-Platform Project: Coded Correspondence.
The focus is on practicing string manipulation, modular arithmetic, and breaking problems into reusable functions.
---

## Ciphers Implemented:
### Caesar Cipher

Shifts each letter in a message by a fixed number of positions in the alphabet.

Functions:

caesar_encode(message, shift)

caesar_decode(message, shift)

### Vigenère Cipher

Uses a keyword to apply a different shift to each letter in the message.

Functions:

vigenere_encode(message, keyword)

vigenere_decode(message, keyword)

### Helper Functions

To keep the code readable and modular, the following helpers were created:

letter_number(letter) – converts letters to numeric indices

number_letter(number) – converts indices back to letters

keyword_shift(keyword) – converts a keyword into numeric shifts

### How to Run
python3 coded_correspondence.py

Modify the message, shift, or keyword in the script to test different cases.

### Skills Practiced

Python functions and loops

Modular arithmetic

String manipulation

Helper function design

Debugging and step-by-step problem solving
