from numa import utils


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
    Information whether the value for iterations needed and the error should be returned or not. Lists starts at iteration two
    since the error is always calculated with respect to the previous guess.

Returns
-------
tuple
    (root value, error, convergence)

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
    convergence = list()
    for n in range(1, max_iterations+1):
        m_n = (a_n + b_n)/2   # Middlepoint
        y_n = function(m_n)   # Function at middle point
        if function(a_n)*y_n < 0:    # root is on left side of m_n
            a_n = a_n
            b_n = m_n         # set new interval end

            err = abs(function(m_n) - 0)
            convergence.append((n, err))
            if err < err_accepted:
                if not giveIterations:
                    return (a_n + b_n)/2, err
                if giveIterations:
                    return (a_n + b_n)/2, err, convergence

        elif function(b_n)*y_n < 0:  # root is on right side of m_n
            a_n = m_n                # set new interval start
            b_n = b_n

            err = abs(function(m_n) - 0)
            convergence.append((n, err))
            if err < err_accepted:
                if not giveIterations:
                    return (a_n + b_n)/2, err
                if giveIterations:
                    return (a_n + b_n)/2, err, convergence

        elif y_n == 0:                     # Exact solution
            if not giveIterations:
                return m_n, 0
            if giveIterations:
                convergence.append((n, 0))
                return m_n, 0, convergence
        else:
            utils.MethodStuckError(
                "Bisection won't converge to root. Please adjust limits."
            )

    raise utils.MaximumIterationError(n)
