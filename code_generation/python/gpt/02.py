def fibonacci(n: int) -> list[int]:
    """
    Return the first n numbers of the Fibonacci sequence.

    Example:
        fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

print(fibonacci(10))
