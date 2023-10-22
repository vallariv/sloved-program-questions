def nth_term_of_ap(a_1, d, n):
    return a_1 + (n - 1) * d

# Example usage:
a_1 = 5  # First term
d = 3    # Common difference
n = 7    # Term number
result = nth_term_of_ap(a_1, d, n)
print(f"The {n}th term of the arithmetic progression is {result}")
