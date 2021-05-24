from numa import utils


def NewtonRhapson(function, x0, Dfunction=None, max_iterations=10000, giveIterations=False):
    """Approximate one root of a given one-parameter function using the Newton-Rhapson method;
note that this method can converge very rapidly with a very good initial value for x0. Though a bad value for x0
can make it impossible to find due to endless cycling between the same points or due to an escape to infinity.


Parameters
----------
function: callable
    Function to analyze.
x0: float
    Initial guess of root value
Dfunction: callable, optional
    Derivative function of the given one-parameter-function
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
Calculates the next x-intercept of the tangent line recursively

.. math::

    x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}

References
-------
 [1] https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
"""
    err_accepted = 10e-15
    convergence = list()
    if Dfunction == None:
        raise Exception(
            "This method currently doesn't support the approximation of derivatives. Please give the derivative function as an input.")
    x_n = x0
    for n in range(1, max_iterations+1):
        y_n = function(x_n)
        if y_n == 0:
            if not giveIterations:
                return x_n, 0
            if giveIterations:
                convergence.append((n, 0))
                return x_n, 0, convergence

        if isinstance(Dfunction, float) or isinstance(Dfunction, int):
            Dy_n = Dfunction
        else:
            Dy_n = Dfunction(x_n)
        if Dy_n == 0:
            raise utils.MethodStuckError("Derivative is zero.")

        if n != 1:
            err = abs(y_old - y_n)
            convergence.append((n, err))
            if err < err_accepted:
                if not giveIterations:
                    return x_n - y_n/Dy_n, err
                if giveIterations:
                    return x_n - y_n/Dy_n, err, convergence
        y_old = y_n
        x_n = x_n - y_n/Dy_n

    raise utils.MaximumIterationError(n)
