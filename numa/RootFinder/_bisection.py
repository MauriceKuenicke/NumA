from numa import Errors


def bisection(function, interval_start, interval_end, max_iterations=10000, giveIterations=False):
    """Approximate one root of a given one-parameter function using the Bisection method;
note that the root has to be inside the interval or the bisection method won't yield any results.
This method can only return one of the possible roots if multiple exist.


Parameters
----------
function: callable
    Function to analyze.
interval_start: int
    lower limit of the domain
interval_end: int
    upper limit of the domain
max_iterations: int
    Maximum number of iterations until the loop breaks. Default set to 10000
giveIterations: boolean, optional
    Information whether the value for iterations needed should be returned or not.

Returns
-------
tuple
    (root value, error, number of iterations)

Notes
-----
Calculates the midpoint after every iteration as

.. math::

    m_N = \\frac{a_N + b_N}{2}

References
-------
 [1] https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/bisection/
"""
    err_accepted = 10e-15
    a_n = interval_start
    b_n = interval_end
    for n in range(1, max_iterations+1):
        m_n = (a_n + b_n)/2   # Middlepoint
        y_n = function(m_n)   # Function at middle point
        if function(a_n)*y_n < 0:    # root is on left side of m_n
            a_n = a_n
            b_n = m_n         # set new interval end
            if n != 1:
                err = abs(y_old - y_n)
                if err < err_accepted:
                    if not giveIterations:
                        return (a_n + b_n)/2, err
                    if giveIterations:
                        return (a_n + b_n)/2, err, n
            y_old = y_n

        elif function(b_n)*y_n < 0:  # root is on right side of m_n
            a_n = m_n         # set new interval start
            b_n = b_n
            if n != 1:
                err = abs(y_old - y_n)
                if err < err_accepted:
                    if not giveIterations:
                        return (a_n + b_n)/2, err
                    if giveIterations:
                        return (a_n + b_n)/2, err, n
            y_old = y_n

        elif y_n == 0:        # Exact solution
            if not giveIterations:
                return m_n, 0
            if giveIterations:
                return m_n, 0, n
        else:
            print("Bisection-Method can't find any roots")
            return None

    raise Errors.MaximumIterationError(n)
