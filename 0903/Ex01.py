def binary_to_int(binary_str: str) -> int:
    result = 0
    for char in binary_str:
        digit = ord(char) - ord('0')
        result = result * 2 + digit
    return result

print(binary_to_int("1010101010101010"))