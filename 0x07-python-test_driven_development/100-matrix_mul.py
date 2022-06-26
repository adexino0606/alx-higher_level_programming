#!/usr/bin/python3
"""
This program takes two matrices and multiply them
"""


def matrix_mul(m_a, m_b):
    """
    Takes two matrices and multiply them
      Args:
        m_a: list of lists (int or float)
        m_b: list of lists (int or float)
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')

    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError('m_b should contain only integers or floats')

    len_row_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_row_a:
            raise TypeError('each row of m_a must be of the same size')

    len_row_b = len(m_b[0])
    for row in m_b:
        if len(row) != len_row_b:
            raise TypeError('each row of m_b must be of the same size')

    len_col_a = len(m_a)
    len_col_b = len(m_b)

    if len_row_a != len_col_b:
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[0 for i in range(len_row_b)] for j in range(len_col_a)]

    for i in range(len_col_a):
        for j in range(len_row_b):
            for k in range(len_col_b):
                new_matrix[i][j] += (m_a[i][k] * m_b[k][j])

    return new_matrix
