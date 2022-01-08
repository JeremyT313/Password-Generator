import string
import random

alphabet = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

characters = alphabet + numbers + symbols

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like in your password? "))
number_of_digits = int(input("How many numbers would you like in your password? "))

selected_letters = random.choices(alphabet, k=number_of_letters)
selected_digits = random.choices(numbers, k=number_of_digits)
selected_symbols = random.choices(symbols, k=number_of_symbols)
selected_characters = selected_letters + selected_digits + selected_symbols

random.shuffle(selected_characters)

password = ''.join(selected_characters)

print(f"Your password is {password}")
