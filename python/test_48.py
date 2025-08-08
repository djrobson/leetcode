from typing import List

import pytest


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    size = len(matrix) - 1
    for shell in range(size):
        for shell_offset in range(size - (2 * shell)):
            top_left = (shell + shell_offset, shell)
            top_right = (size - shell, shell + shell_offset)
            bottom_right = (size - shell - shell_offset, size - shell)
            bottom_left = (shell, size - shell - shell_offset)

            old_top_left = matrix[top_left[1]][top_left[0]]

            matrix[top_left[1]][top_left[0]] = matrix[bottom_left[1]][bottom_left[0]]
            matrix[bottom_left[1]][bottom_left[0]] = matrix[bottom_right[1]][
                bottom_right[0]
            ]
            matrix[bottom_right[1]][bottom_right[0]] = matrix[top_right[1]][
                top_right[0]
            ]
            matrix[top_right[1]][top_right[0]] = old_top_left


def test_1x1():
    input = [[1]]
    rotate(input)
    assert input == [[1]], "Failed with a 1x1 matrix"


def test_2x2():
    input = [[1, 2], [3, 4]]
    rotate(input)
    assert input == [[3, 1], [4, 2]], "Failed with a 2x2 matrix"


def test_3x3():
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(input)
    assert input == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "Failed with a 3x3 matrix"


def test_4x4():
    input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate(input)
    assert input == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ], "Failed with a 4x4 matrix"
