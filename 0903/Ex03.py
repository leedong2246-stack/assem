def int_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    
    digits = []
    curr = n
    while curr > 0:
        remainder = curr % 2
        digits.append(chr(ord('0') + remainder))
        curr //= 2
    return "".join(reversed(digits))

print(int_to_binary(43690))