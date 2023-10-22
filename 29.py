total = 0
while True:
    num = input("Enter a number (q to quit): ")
    if num == 'q':
        break
    total += float(num)
print(f"Sum of numbers: {total}")
