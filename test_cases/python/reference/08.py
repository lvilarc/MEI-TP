import math

def getPermutation(n, k):
    numbers = list(range(1, n + 1))
    k -= 1
    out = []
    for size in range(n, 0, -1):
        fact = math.factorial(size - 1)
        idx, k = divmod(k, fact)
        out.append(str(numbers.pop(idx)))
    return ''.join(out)
