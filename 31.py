n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
