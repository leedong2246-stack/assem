def int_to_hex(n: int) -> str:
    if n == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    digits = []
    curr = n
    while curr > 0:
        remainder = curr % 16
        digits.append(hex_chars[remainder])
        curr //= 16
        
    return "".join(reversed(digits))

print(int_to_hex(439041101)) 