"""https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python"""

from collections import defaultdict

def simplify(poly: str):
    number_start_index = None
    symbols_start_index = None
    current_sign = 1
    symbols_grouped = defaultdict(int)
    END_SYMBOL = '|'
    for index, char in enumerate(poly + END_SYMBOL):

        if char in ['+', '-', END_SYMBOL]:
            new_sign = 1 if char == '+' else -1
            if index == 0:
                current_sign = new_sign
                continue

            if number_start_index is not None:
                number = int(poly[number_start_index:symbols_start_index]) * current_sign
            else:
                number = current_sign

            symbols = ''.join(sorted(poly[symbols_start_index:index]))
            symbols_grouped[symbols] += number

            number_start_index = None
            symbols_start_index = None
            current_sign = new_sign
        if char.isnumeric():
            number_start_index = number_start_index or index
        if char.isalpha():
            symbols_start_index = symbols_start_index or index
    return symbols_grouped


res = simplify('-a+5ab+3a-c-2a')
assert res == '5b-a'
