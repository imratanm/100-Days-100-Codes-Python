print("Welcome to Password Generator")

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-','/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

password_length = int(input("Enter how many digits password you want to generate: "))

password_list = []

letters_in_password = (password_length // 2)
numbers_in_password = ( password_length // 3)
symbols_in_password = password_length - (letters_in_password + numbers_in_password)

for _ in range(letters_in_password):
    password_list.append(random.choice(letters))
for _ in range (numbers_in_password):
    password_list.append(random.choice(numbers))
for _ in range (symbols_in_password):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your Genretated Password is : {password}")
