N = int(input("Enter a positive integer N: "))
sum_even = 0
for i in range(2, N + 1, 2):
    sum_even += i
print(f"The sum of even numbers between 1 and {N} is {sum_even}")
