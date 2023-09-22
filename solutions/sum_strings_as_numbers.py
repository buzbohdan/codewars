"""https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/python"""

def sum_strings(x: str, y: str) -> str:
    max_length = max(len(x), len(y))
    x = x.rjust(max_length, '0')
    y = y.rjust(max_length, '0')
    result = []
    extra = 0
    for i in range(max_length - 1, -1, -1):
        sum = ord(x[i]) + ord(y[i]) + extra - 96
        result.append(chr(sum % 10 + 48))
        extra = sum // 10
    if extra:
        result.append('1')
    return ''.join(reversed(result)).lstrip('0') or '0'

a = sum_strings('0099', '1')
pass