def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return num == sum(divisors)

num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
