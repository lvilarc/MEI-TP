from typing import Sequence

Matrix3x3 = Sequence[Sequence[float]]

def multiply_3x3_matrices(a: Matrix3x3, b: Matrix3x3) -> list[list[float]]:
    """
    Multiply two 3x3 matrices.

    Args:
        a: First 3x3 matrix.
        b: Second 3x3 matrix.

    Returns:
        The resulting 3x3 matrix.

    Raises:
        ValueError: If either matrix is not 3x3.
    """
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Both matrices must have exactly 3 rows.")

    if any(len(row) != 3 for row in a) or any(len(row) != 3 for row in b):
        raise ValueError("Both matrices must be 3x3.")

    result = [[0.0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += a[i][k] * b[k][j]

    return result

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = multiply_3x3_matrices(matrix_a, matrix_b)

for row in result:
    print(row)