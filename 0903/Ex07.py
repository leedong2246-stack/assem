def multiply_hex_digit(digit: str, hex_str: str) -> str:
    def char_to_val(c):
        c = c.upper()
        if '0' <= c <= '9':
            return ord(c) - ord('0')
        return ord(c) - ord('A') + 10

    single_val = char_to_val(digit)
    
    if single_val == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    carry = 0
    result = []

    for i in range(len(hex_str) - 1, -1, -1):
        v = char_to_val(hex_str[i])
        prod = (v * single_val) + carry
        carry = prod // 16
        result.append(hex_chars[prod % 16])
    if carry > 0:
        result.append(hex_chars[carry])
    res_str = "".join(reversed(result)).lstrip('0')
    return res_str if res_str else "0"
print(multiply_hex_digit("A", "1A2B")) 