# _*_ coding:utf-8 _*_

"""
This file is about ways to get nth column from array
"""
import numpy as np


def get_nth_column():
    """
    this is about how to get nth column from array
    :return:none
    """
    arr = np.arange(9).reshape((3, 3))
    print arr
    # [[0 1 2]
    #  [3 4 5]
    #  [6 7 8]]
    arr_c2 = arr[:, [0, 2]]  # arr_c2 deep copy from arr
    print arr_c2
    # [[0 2]
    #  [3 5]
    #  [6 8]]
    arr_c2[:, [0]] = 9
    print arr  # no change, as we see this is deep copy
    print arr_c2
    # [[9 2]
    #  [9 5]
    #  [9 8]]
    arr_c1 = arr[:, 0]
    print arr_c1
    # [0 3 6]
    arr_c11 = arr[:, [0]]
    print arr_c11
    # [[0]
    #  [3]
    #  [6]]


def get_nth_row():
    """
    get nth row
    :return: none
    """
    arr = np.arange(12).reshape(3, 4)
    print arr
    # [[ 0  1  2  3]
    #  [ 4  5  6  7]
    #  [ 8  9 10 11]]
    print arr[1, :]   # or just arr[1]
    # [4 5 6 7]


def change_nth_col_value():
    """
    change nth column value by condition
    :return:
    """
    arr = np.arange(12).reshape(4, 3)
    print arr
    a_col = arr[:, 0]
    print a_col
    # [0 3 6 9]
    print [a if a % 2 else 111 for a in arr[:, 0]]
    # [111, 3, 111, 9]
    print arr  # no change
    # [[ 0  1  2]
    #  [ 3  4  5]
    # [ 6  7  8]
    # [ 9 10 11]]

    for i in xrange(arr.shape[0]):
        if arr[i][0] % 2 == 0:
            arr[i][0] = 111

    print arr
    # [[111   1   2]
    #  [  3   4   5]
    # [111   7   8]
    # [  9  10  11]]

    arr = np.arange(12).reshape(4, 3)
    print [arr[i][0] if arr[i][0] % 2 else 111 for i in xrange(arr.shape[0])]
    # [111, 3, 111, 9]
    print arr
    # [[ 0  1  2]
    #  [ 3  4  5]
    # [ 6  7  8]
    # [ 9 10 11]]


if __name__ == '__main__':
    # get_nth_column()
    # get_nth_row()
    change_nth_col_value()