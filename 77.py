my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print("Dictionary after removing the key:", my_dict)
