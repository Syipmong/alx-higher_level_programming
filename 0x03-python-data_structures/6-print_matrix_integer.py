#!/usr/bin/python3
"""give a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    transposed = []
    for row in matrix:
        tran_row = []
        for i in row:
            tran_row.append(i)
        transposed.append(tran_row)
    for row in transposed:
        print(" ".join("{:d}".format(i) for i in row))
