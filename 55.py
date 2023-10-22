my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 20}
max_key = max(my_dict, key=my_dict.get)
max_value = my_dict[max_key]
print("Key with the maximum value:", max_key)
print("Maximum value:", max_value)
