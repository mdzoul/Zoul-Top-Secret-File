import random
from let_num_sym import *

print("\n\33[32m---Welcome to the PyPassword Generator!---\33[0m")

# nr_letters= int(input("How many letters would you like in your password?\n")) 
# random_letters = random.choices(letters, k=nr_letters)

# nr_symbols = int(input(f"How many symbols would you like?\n"))
# random_symbols = random.choices(symbols, k=nr_symbols)
# # print(random_symbols)

# nr_numbers = int(input(f"How many numbers would you like?\n"))
# random_numbers = random.choices(numbers, k=nr_numbers)
# # print(random_numbers)

# combine_letnumsym = random_letters + random_symbols + random_numbers
# # print(type(combine_letnumsym))

# randomized_letnumsym = random.sample(combine_letnumsym, len(combine_letnumsym))
# # print(randomized_letnumsym)
# # print(type(randomized_letnumsym))

total_letnumsym = letters + numbers + symbols
random_letnumsym = random.choices(total_letnumsym, k=12)
new_password = ''.join(random_letnumsym)

print(f"Your new password is: \33[1m{new_password}\33[0m\n")