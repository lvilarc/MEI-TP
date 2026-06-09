def decimal_to_binary(n: int) -> str:
    if n < 0:
        return "-" + bin(-n)[2:]
    return bin(n)[2:]  # strip the '0b' prefix

# Examples
print(decimal_to_binary(0))   # "0"
print(decimal_to_binary(10))  # "1010"
print(decimal_to_binary(255)) # "11111111"