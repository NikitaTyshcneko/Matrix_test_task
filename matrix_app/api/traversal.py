from typing import List


def traverse_matrix(matrix: List[List[int]]) -> List[List[int]]:
    return list(zip(*matrix))
