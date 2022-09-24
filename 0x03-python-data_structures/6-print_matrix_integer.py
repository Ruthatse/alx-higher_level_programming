#!/usr/bin/python3
# 6-print_matrix_integer.py
# Ruth Atse <ruth.atse4@gmail.com>


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
