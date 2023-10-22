list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
unique_list = list(set(item for sublist in list_of_lists for item in sublist))
print("List of unique elements from a list of lists:", unique_list)
