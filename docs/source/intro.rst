Introduction
============

``NumA`` is a Python package that contains some very useful
functions for numerical analysis. As an example, we can approximate the root of a given function
using the Bisection method. As an example, we can calculate the root for :math:`f(x) = 3x-3` on the interval :math:`[-3,5]`::

       >>> import numa
       >>> f = lambda x: 3*x-3
       >>> numa.RootFinder.bisection(f, -3, 5)
       # (1.0, 0)

Similarly, we can do a basic 1D pre analysis in :math:`[-100,100]` of possible root values to help define needed interval limits:

.. code-block:: python

   >>> f = lambda x: x**2 - 5*x +3
   >>> numa.RootFinder.preAnalysis1D(f, -100, 100)
   # Possible roots found at around x = 0.6990069900698899,4.3030430304303025


``NumA`` also includes methods like Gauss and LU-decomposition to solve systems of linear equations in the ``numa.LinearSystem`` submodule.

.. code-block:: python

   >>> import numpy as np
   >>> import numa
   >>> A = np.array([[7, -1, 0], [4, 6, -3],[-2, 6, 1]], dtype=float)
   >>> b = np.array([5, 7, 13], dtype=float)
   >>> numa.LinearSystem.solveGauss(A, b) 
   # array([1., 2., 3.])
   >>> numa.LinearSystem.solveLU(A, b)
   # array([1., 2., 3.])