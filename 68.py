dict1 = {'a': 3, 'b': 5, 'c': 2}
dict2 = {'b': 2, 'c': 7, 'd': 1}
merged_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print("Merged dictionary with summed values for common keys:")
print(merged_dict)
