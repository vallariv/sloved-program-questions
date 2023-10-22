numbers = [12, 34, 56, 78, 90]
element = int(input("Enter the number to check: "))
if element in numbers:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")
