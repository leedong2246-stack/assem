def add_base_b(s1: str, s2: str, b: int) -> str:
    i = len(s1) - 1
    j = len(s2) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry > 0:
        d1 = ord(s1[i]) - ord('0') if i >= 0 else 0
        d2 = ord(s2[j]) - ord('0') if j >= 0 else 0
        
        total = d1 + d2 + carry
        carry = total // b
        current_digit = total % b
        
        result.append(chr(ord('0') + current_digit))
        
        i -= 1
        j -= 1
        
    return "".join(reversed(result))
print(add_base_b("123", "456", 7)) 