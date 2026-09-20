def hex_to_int(hex_str: str) -> int:
    result = 0
    for char in hex_str:
        c = char.upper()
        if '0' <= c <= '9':
            digit = ord(c) - ord('0')
        elif 'A' <= c <= 'F':
            digit = ord(c) - ord('A') + 10
        else:
            raise ValueError("유효하지 않은 16진수 문자입니다.")
        
        result = result * 16 + digit
    return result

print(hex_to_int("1A2B3C4D")) 