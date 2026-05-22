# generate full name
# generate age
# generate zipcode
import os

# data directory
generated_data = "generated_data"

first_names = []
last_names = []

with open(os.path.join(generated_data, "first-names.txt"), "r") as f:
    first_names = f.read().splitlines()

with open(os.path.join(generated_data, "last-names.txt"), "r") as f:
    last_names = f.read().splitlines()

print("\n=================================")
print("FIRST NAMES AND LAST NAMES")
print("=================================\n")

print(first_names)
print()
print(last_names)

print("\n=================================")
print("GENERATED FULL NAMES")
print("=================================\n")

print("IN PROGRESS...")
