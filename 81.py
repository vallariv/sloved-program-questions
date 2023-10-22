my_list = [1, 2, 2, 3, 4, 2, 5, 6]
element_to_remove = 2
filtered_list = [x for x in my_list if x != element_to_remove]
print("List after removing all occurrences of", element_to_remove, ":", filtered_list)
