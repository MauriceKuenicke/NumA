import numpy as np
from numa.LinearSystem import LU, solveGauss, solveLU


class MaximumIterationError(Exception):
    """Exception raised when the maximum number of iterations is reached.

    Attributes:
        iterations -- input salary which caused the error
    """

    def __init__(self, iterations):
        self.iterations = iterations
        self.message = f"Maxmimum number of {self.iterations} iterations reached"
        super().__init__(self.message)


class MethodStuckError(Exception):
    """Exception raised when a method is stuck. E.g. a zero-derivative during the Newton-Rhapson-Method.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, reason):
        self.reason = reason
        self.message = f"Method is stuck. Reason given: {self.reason}"
        super().__init__(self.message)


class DimensionError(Exception):
    """Exception raised when the dimension numbers don't match.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, reason):
        self.reason = reason
        self.message = f"{self.reason}"
        super().__init__(self.message)


class SingularityError(Exception):
    """Exception raised when matrix is singular.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, reason):
        self.reason = reason
        self.message = f"{self.reason}"
        super().__init__(self.message)


def _checkDimensions(A, b):
    if not A.shape[0] == A.shape[1]:
        raise DimensionError("Input matrix A is not quadratic!")
    if not b.shape[0] == A.shape[1]:
        raise DimensionError("Dimensions of A and b do not match!")


def det(A):
    """Returns determinant of A.

Parameters
----------
A: numpy.arrays
    Matrix

Returns
-------
D: numpy.arrays
    Determinant

Notes
-----
Currently this function is only calling the numpy function under the hood until the LU problems are fixed.

"""
    return np.linalg.det(A)


def isSingular(A):
    """Checks if matrix A is singular or not.

Parameters
----------
A: numpy.arrays
    Matrix

Returns
-------
T,F: boolean
    True if matrix is singular, False if not.

Notes
-----
Currently only checks determinant.

"""
    if np.allclose(det(A), 0., atol=10e-14):
        return True
    else:
        return False


def inverse(A):
    """Calculates the inverse matrix of A such that

.. math::

    A \cdot A^{-1} = I

Parameters
----------
A: numpy.arrays
    Matrix

Returns
-------
inverseA: numpy.arrays
    Inverse matrix of A

"""
    m, n = A.shape
    if not m == n:
        raise DimensionError("Input matrix A is not quadratic!")
    if isSingular(A):
        raise SingularityError("Input matrix is singular.")
    I = np.identity(m)
    inverseA = np.zeros((m, m))

    for i in range(m):
        b = I[:, i]
        x = solveLU(A, b)
        inverseA[:, i] = x
    return inverseA
