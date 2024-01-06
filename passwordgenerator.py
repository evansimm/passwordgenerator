# Python Project: Password Creator

import random

# Character sets for the password
capitalLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowerLetters = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
specialCharacters = "?,.<>!%$[]}{*)(|@#%^&-_=+"

# Set the character sets to be used
capital,lower,digits,special = True,True,True,True

# Initialize the final string of characters to be used in the password
finalPassword = ""

# Add the character sets to the final string of characters
if capital:
    finalPassword += capitalLetters
if lower:
    finalPassword += lowerLetters
if digits:
    finalPassword += numbers
if special:
    finalPassword += specialCharacters

# Set the length and quantity of the password
passwordLength = 16
passwordQuantity = 10

# Create the password then print it
for x in range(passwordQuantity):
    password = "".join(random.sample(finalPassword,passwordLength))
    print(password)