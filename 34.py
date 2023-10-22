def prime_factors(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors

num = int(input("Enter a number: "))
factors = prime_factors(num)
print(f"Prime factors of {num}: {factors}")
