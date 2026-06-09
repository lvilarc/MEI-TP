def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n using recursion."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Example usage
print(factorial(5))  # 120