my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
max_value = max(my_dict.values())
keys_with_max_value = [k for k, v in my_dict.items() if v == max_value]
print("Keys with the highest value:", keys_with_max_value)
