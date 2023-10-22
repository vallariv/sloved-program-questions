principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = int(input("Enter the number of years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + rate/n)**(n*time)
interest = amount - principal
print(f"The total amount is {amount:.2f}, and the interest is {interest:.2f}")
