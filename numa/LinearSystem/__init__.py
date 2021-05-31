from ._gauss import solveGauss
from ._LU import LU, solveLU
from numa import utils
import numpy as np


def condition(A, p):
    """Calculate the condition number of the input Matrix using the numpy function.


Parameters
----------
A: numpy.arrays
    Input matrix whose condition number is sought 
p: {None, 1, -1, 2, -2, inf, -inf, 'fro'}
    Order of the norm

Returns
-------
c: float
    Condition number of the matrix. May be infinite.

"""
    return np.linalg.cond(A, p=p)
