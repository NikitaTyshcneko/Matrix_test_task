from typing import List


def traverse_matrix(matrix: List[List[int]]) -> List[List[int]]:
    result = []
    while matrix:
        result.extend(matrix.pop(0))
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result.extend(matrix.pop()[::-1])
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    n = len(result) ** 0.5
    n = int(n)
    return [result[i:i + n] for i in range(0, len(result), n)]
