import numpy as np
from numa import utils


def solveGauss(A, b):
    """Solves the given linear system of equations using the Gauss method. A post-iteration is implemented as well
to reduce the error.


Parameters
----------
A: numpy.arrays
    Coefficient matrix 
b: numpy.array
    Column vector of constant terms

Returns
-------
x: numpy.array
    Solution vector

Notes
-----
The pivot element for the i-th row in the i-th column is choosen through

.. math::

    a_p = max_{k=i,...,n}|a_{ki}|

Rounding errors can lead to less accurate results so

.. math::

    A \cdot (x + \Delta x) = b + \Delta b

is calculated instead. This can be rewritten 

.. math::

    \Delta b = A \cdot (x + \Delta x) - b 

.. math::

    A \cdot \Delta x = \Delta b

.. math::

    x_0 = (x + \Delta x)

.. math::

    x_1 = x_0 - \Delta x

"""
    utils._checkDimensions(A, b)
    if utils.isSingular(A):
        raise utils.SingularityError("Input matrix is singular.")
    x_calculated = _gauss(A, b)

    acc = 10e-14
    accuracy_achieved = False
    while not accuracy_achieved:
        delb = b - np.matmul(A, x_calculated)
        delX = _gauss(A, delb)
        x_calculated = np.subtract(x_calculated, delX)
        if [x < acc for x in x_calculated]:
            accuracy_achieved = True
    return x_calculated


def _gauss(A, b):
    """Python implementation of the Gauß method to solve systems of linear equations.


Parameters
----------
A: numpy.arrays
    Coefficient matrix 
b: numpy.array
    Column vector of constant terms

Returns
-------
x: numpy.array
    Solution vector

"""
    M = np.column_stack((A, b))
    m, n = M.shape
    for j in range(n-1):
        # i - row, j - column
        pivot_elements = [abs(M[l][j]) for l in range(j, len(M))]
        pivot_index = pivot_elements.index(max(pivot_elements)) + j
        pivot_row, j_row = np.copy(M[pivot_index]), np.copy(M[j])
        M[j], M[pivot_index] = pivot_row, j_row                     # Swap

        for i in range(j+1, m):
            f = M[i][j] / M[j][j]
            for k in range(j + 1, n):
                M[i][k] -= M[j][k] * f
            M[i][j] = 0

    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, M[i][m] / M[i][i])
        for k in range(i - 1, -1, -1):
            M[k][m] -= M[k][i] * x[0]
    return x
