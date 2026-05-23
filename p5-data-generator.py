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

total_first_names = len(first_names)

with open(os.path.join(generated_data, "last-names.txt"), "r") as f:
    last_names = f.read().splitlines()

for i in range(total_first_names):
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

for i in range(total_first_names):
    age = int(random.triangular(18, 65, 25))
    ages.append(age)
    print(age)

print("\nRAW LIST\n==========")
print(ages)

print("\n==============================")
print("|||| ZIP CODE GENERATOR ||||")
print("==============================\n")
zip_codes = []

with open(os.path.join(generated_data, "zip-codes.txt"), "r") as f:
    zip_codes = f.read().splitlines()

for i in range(total_first_names):
    print(zip_codes[i])

print("\nRAW LIST\n==========")
print(zip_codes)

# ===================================
# |||| USER DICTIONARY GENERATOR ||||
# ===================================
