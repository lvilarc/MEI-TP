def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(0))   # 1