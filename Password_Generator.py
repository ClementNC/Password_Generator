import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
num_letters = 0
while num_letters <= 0:
    num_letters = int(input("How many letters would you like in your password?\n"))
    if num_letters <= 0:
        print("There must be at least one letter in the password")
num_symbols = 0
while num_symbols <= 0:
    num_symbols = int(input("How many symbols would you like?\n"))
    if num_symbols <= 0:
        print("There must be at least one symbol in the password")
num_numbers = 0
while num_numbers <= 0:
    num_numbers = int(input("How many numbers would you like?\n"))
    if num_numbers <= 0:
        print("There must be at least one number in the password")
password = ""

# This loop will take randomly num_letters amount of letters from the list of letters above
for i in range(num_letters):
    password += random.choice(letters)

# This loop will take randomly num_symbols amount of symbols from the list of symbols above
for i in range(num_symbols):
    password += random.choice(symbols)

# This loop will take randomly num_numbers amount of numbers from the list of symbols above
for i in range(num_numbers):
    password += random.choice(numbers)

# The line of code below will shuffle the arrangement of the characters in the password.
password = random.sample(password, len(password))
password = ''.join(password)

print(f"Your password is {password}")