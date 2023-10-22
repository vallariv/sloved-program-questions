def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

my_list = [1, 2, 3, 4, 5]
is_sorted = is_sorted_ascending(my_list)
print("Is the list sorted in ascending order?", is_sorted)
