import random
from let_num_sym import *

print("\n\33[32m---Welcome to Zoul's PIN Code Generator!---\33[0m")

random_pin = random.choices(numbers, k=6)
new_password = ''.join(random_pin)

print(f"Your new PIN code is: \33[1m{new_password}\33[0m\n")