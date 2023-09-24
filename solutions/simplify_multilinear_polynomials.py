"""https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python"""

from collections import defaultdict

# A special symbol that will be added to the end of the polynomial to simplify
# logic of processing the last element
END_SYMBOL = "|"


def simplify(poly: str) -> str:
    number_start_index: int | None = None
    symbols_start_index: int | None = None
    sign: str | None = None
    coefficients: dict[str, int] = defaultdict(int)

    for index, char in enumerate(poly + END_SYMBOL):
        if char in ["+", "-", END_SYMBOL]:
            if index == 0:
                sign = char
                continue

            if number_start_index is not None:
                coefficient = int(poly[number_start_index:symbols_start_index])
            else:
                coefficient = 1
            if sign == "-":
                coefficient = -coefficient

            symbols = "".join(sorted(poly[symbols_start_index:index]))
            coefficients[symbols] += coefficient

            number_start_index = None
            symbols_start_index = None
            sign = char

        if char.isnumeric() and number_start_index is None:
            number_start_index = index

        if char.isalpha() and symbols_start_index is None:
            symbols_start_index = index

    result_fragments: list[str] = []

    # Sort all symbols by number of variables and then in the lexigraphic order
    sorted_symbols = sorted(coefficients, key=lambda symbols: (len(symbols), symbols))
    for symbols in sorted_symbols:
        coefficient = coefficients[symbols]
        if coefficient == 0:
            continue

        sign = "-" if coefficient < 0 else ("" if not result_fragments else "+")
        number_in_fragment = abs(coefficient) if abs(coefficient) != 1 else ""
        result_fragments.append(f"{sign}{number_in_fragment}{symbols}")

    return "".join(result_fragments)
