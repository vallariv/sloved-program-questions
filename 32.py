n = int(input("Enter the number of rows (odd number): "))
for i in range(1, n, 2):
    print(" " * ((n - i) // 2) + "*" * i)
for i in range(n, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
