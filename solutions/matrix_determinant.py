def determinant(matrix):

    def _determinant(y: int, previous_columns: list[int]) -> int:
        """Recursively computes determinant for a submatrix of the initial matrix

        Args:
            y: index of a matrix' row that we're processing in this iteration
                we start at the first row (y = 0) and move down to the last row
            previous_columns: list of indices of columns for which we currently
                compute the determinant. Such columns should be excluded from the
                computation
        """
        sign = 1
        result = 0
        for x, value in enumerate(matrix[y]):
            if x in previous_columns:
                continue
            # We're at the last row, so we're dealing with 1*1 matrices and can just
            # return the value. This is also an exit point for our recursive approach
            if y == len(matrix) - 1:
                return value
            result += value * _determinant(y + 1, previous_columns + [x]) * sign
            sign *= -1
        return result

    return _determinant(0, [])

d = determinant([[5]])
assert d == 5

d = determinant([
    [5, 2],
    [3, 6],
])
assert d == 5 * 6 - 2 * 3
