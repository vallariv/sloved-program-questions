dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
merged_dict = {key: [dict1.get(key), dict2.get(key)] for key in set(dict1) | set(dict2)}
print("Merged dictionary with concatenated values for duplicate keys:")
print(merged_dict)
