my_string = "abracadabra"
for char in my_string:
    if my_string.count(char) == 1:
        first_non_repeated = char
        break
print("First non-repeated character in the string:", first_non_repeated)
