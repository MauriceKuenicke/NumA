import numpy as np
from numa import utils


def solveLU(A, b):
    """Solves the given linear system of equations using LU decomposition. A post-iteration is implemented as well
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

"""
    utils._checkDimensions(A, b)
    L, U = LU(A)
    x_calculated = _solveX(L, U, b)

    acc = 10e-14
    accuracy_achieved = False
    while not accuracy_achieved:
        delb = b - np.matmul(A, x_calculated)
        delX = _solveX(L, U, delb)
        x_calculated = np.subtract(x_calculated, delX)
        if [x < acc for x in x_calculated]:
            accuracy_achieved = True
    return x_calculated


def _solveX(L, U, b):
    """Use forward and backwards substitution to calculate the x vector to solve the linear system of equations.


Parameters
----------
L: numpy.arrays
    Lower triangular matrix
U: numpy.arrays
    Upper triangular matrix
b: numpy.array
    Column vector of constant terms

Returns
-------
x: numpy.array
    Solution vector

"""
    m, n = L.shape
    # Forward Substitution
    y = list()
    y.insert(0, b[0]/L[0][0])
    for i in range(1, m):
        summ = 0
        for k in range(0, i):
            summ += L[i][k]*y[k]
        y.insert(i, (b[i]-summ)/(L[i][i]))

    # Backwards Substitution
    x = [0]*m
    x[m-1] = y[m-1] / U[m-1][m-1]
    for i in range(m - 2, -1, -1):
        summ = 0
        for k in range(i+1, n):
            summ += U[i][k]*x[k]
        x[i] = (y[i] - summ)/U[i][i]

    return x


def LU(A):
    """Decompose the given coefficient matrix into a lower and upper triangular matrix L and U so that

.. math::

    A = L \cdot U


Parameters
----------
A: numpy.arrays
    Matrix

Returns
-------
L, U: numpy.arrays
    Lower and upper triangular matrix.

Notes
-----
The decomposition is calculated using Doolittle's method.

.. math::     l_{ii} = 1

.. math::     u_{ij} = a_{ij} - \sum_{k=1}^{i-1}l_{ik}u_{kj}

.. math::     l_{ji} = u_{ii}^{-1}(a_{ij} - \sum_{k=1}^{i-1}l_{jk}u_{ki})

"""
    m, n = A.shape
    L, U = np.zeros([m, n]), np.zeros([m, n])
    for i in range(n):
        L[i][i] = 1

    for i in range(n):

        # Upper triangular matrix
        for j in range(i, n):
            summ = 0
            for k in range(0, i):
                summ += L[i][k]*U[k][j]
            U[i][j] = A[i][j] - summ

        # Lower triangular matrix
        for j in range(i+1, n):
            summ = 0
            for k in range(0, i):
                summ += L[j][k]*U[k][i]
            L[j][i] = (A[j][i] - summ)/U[i][i]
    return L, U
