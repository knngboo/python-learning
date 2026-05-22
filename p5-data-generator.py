import pandas as pd

# Create a sample DataFrame
# var = {"key1": ["value1"],
#        "key2": ["value1", "value2"],
#        "key3": ["value1", "value2", "value3"]}
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
#
df_data = pd.DataFrame(data)
print(df_data)
