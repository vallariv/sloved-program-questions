dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 20, 'd': 40, 'e': 50}
common_elements = set(dict1.keys()) & set(dict2.keys())
print("Common keys between the two dictionaries:", common_elements)
