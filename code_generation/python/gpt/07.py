def gcd(a: int, b: int) -> int:
    """
    Find the Greatest Common Divisor of two integers using
    the Euclidean algorithm.
    """
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


# Example usage
num1 = 48
num2 = 18

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")