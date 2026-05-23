# generate full name
# generate age
# generate zipcode
# generate user dictionary
print("\n================================")
print("|||| FULL NAME GENERATOR ||||")
print("================================\n")
import os

# data directory
generated_data = "generated_data"

first_names = []
last_names = []
full_names = []

with open(os.path.join(generated_data, "first-names.txt"), "r") as f:
    first_names = f.read().splitlines()

with open(os.path.join(generated_data, "last-names.txt"), "r") as f:
    last_names = f.read().splitlines()

for i in range(32):
    full_name = first_names[i] + " " + last_names[i]
    full_names.append(full_name)
    print(full_name)

print("\nRAW LIST\n==========")
print(full_names)

print("\n========================")
print("|||| AGE GENERATOR ||||")
print("========================\n")

import random

ages = []

for i in range(32):
    age = int(random.triangular(18, 65, 25))
    ages.append(age)
    print(age)

print("\nRAW LIST\n==========")
print(ages)

# ===============================
# |||| ZIP CODE GENERATOR ||||
# ===============================

# ===================================
# |||| USER DICTIONARY GENERATOR ||||
# ===================================
