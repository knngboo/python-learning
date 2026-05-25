import pandas as pd

# Create a sample DataFrame (using python dictionary)
# python dictionary is a list of keys with lists of values
# var = {"key1": ["value1"],
#        "key2": ["value1", "value2"],
#        "key3": ["value1", "value2", "value3"]}
users_csv = {
    "Membership": [],
    "Age": [],
    "Name": [],
    "Zip Code": [],
    "Trips": [],
    "From": [],
    "To": [],
}
# Create a DataFrame from the dictionary
# use pd.DataFrame() to create a DataFrame
df_data = pd.DataFrame(users_csv)

print(df_data)
