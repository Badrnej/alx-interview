#!/usr/bin/python3

"""Rotating 2D matrix in place"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix in place"""

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
