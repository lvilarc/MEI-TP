def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(18))  # False
print(is_prime(1))   # False