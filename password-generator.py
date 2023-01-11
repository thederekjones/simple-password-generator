import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('''
  _____         _____                                           _ 
 |  __ \       |  __ \                                         | |
 | |__) |_   _ | |__) |__ _  ___  ___ __      __ ___   _ __  __| |
 |  ___/| | | ||  ___// _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |
 | |    | |_| || |   | (_| |\_ _\\\__ \ \ V  V /| (_) || |  | (_| |
 |_|     \__, ||_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|
          __/ |                                                   
         |___/                                                    
\n''')
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Set empty list to hold characters for password
pass_characters = []

# Loop through letters list and append a random letter to the empty list.
for letter in range(nr_letters):
  random_number = random.randint(0, len(letters) - 1)
  pass_characters.append(letters[random_number])

# Loop through symbols list and append a random symbol to the empty list.
for symbol in range(nr_symbols):
  random_number = random.randint(0, len(symbols) - 1)
  pass_characters.append(symbols[random_number])

# Loop through numbers list and append a random number to the empty list.
for number in range(nr_numbers):
  random_number = random.randint(0, len(numbers) - 1)
  pass_characters.append(numbers[random_number])

# Loop through the pass_characters list, pop off a random character, and place the character back in randomly.
for char in range(len(pass_characters)):
  random_number = random.randint(0, len(pass_characters) - 1)
  rearrange = pass_characters.pop(random_number)
  pass_characters.append(rearrange)

# Set empty string to hold randomly generated password.
password = ""

# Loop through the pass_characters list and add it in order to empty list.
for char in range(len(pass_characters)):
  password += pass_characters[char]

print(f"Your new password is: {password}")