# Task -> Generate a random integer between 1 and 100 and check if the result is an even number.

import random

x = random.randint(1, 100)
if x%2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")