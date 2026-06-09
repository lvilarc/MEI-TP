import math

def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, False otherwise."""
    if n < 2:
        return False          # 0 and 1 are not prime
    if n == 2:
        return True           # 2 is the only even prime
    if n % 2 == 0:
        return False          # eliminate all other even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # check odd divisors only
        if n % i == 0:
            return False
    return True

print(is_prime(1))   # False
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(18))  # False
print(is_prime(97))  # True