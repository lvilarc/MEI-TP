def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))   # Output: 6
print(gcd(100, 75))  # Output: 25