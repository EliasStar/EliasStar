def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = input("Factorial of: ")

print(factorial(n))
