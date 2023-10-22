from collections import Counter

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
mode_element = Counter(my_list).most_common(1)[0][0]
print("Mode of the list:", mode_element)
