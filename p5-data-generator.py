# generate full name
# generate age
# generate zipcode
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

print("\n=================================")
print("FIRST NAMES")
print("=================================\n")

for x in first_names:
    print(x)

print("\n=================================")
print("LAST NAMES")
print("=================================\n")

for x in last_names:
    print(x)

print("\n=================================")
print("GENERATED FULL NAMES")
print("=================================\n")

for i in range(32):
    full_name = first_names[i] + " " + last_names[i]
    print(full_name)
