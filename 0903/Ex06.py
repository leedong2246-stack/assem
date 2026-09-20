def add_hex(s1: str, s2: str) -> str:
    def char_to_val(c):
        c = c.upper()
        if '0' <= c <= '9':
            return ord(c) - ord('0')
        return ord(c) - ord('A') + 10

    hex_chars = "0123456789ABCDEF"
    i = len(s1) - 1
    j = len(s2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry > 0:
        d1 = char_to_val(s1[i]) if i >= 0 else 0
        d2 = char_to_val(s2[j]) if j >= 0 else 0

        total = d1 + d2 + carry
        carry = total // 16
        result.append(hex_chars[total % 16])

        i -= 1
        j -= 1

    return "".join(reversed(result))
print(add_hex("1A2B", "3C4D")) 