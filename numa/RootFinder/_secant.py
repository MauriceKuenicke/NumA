def f(x): return x**2 - x - 1


def secant(function, interval_start, interval_end, max_iterations=10000, giveIterations=False):
    """Approximate one root of a given one-parameter function using the secant method;

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

"""
    err_accepted = 10e-15
    a_n = interval_start
    b_n = interval_end
    for n in range(1, max_iterations+1):
        x_k = _calcX_k(function, a_n, b_n)   # Crossing point
        y_n = function(x_k)                  # Function value at crossing point

        if y_n == 0:                     # Exact solution
            if not giveIterations:
                return x_k, 0
            if giveIterations:
                return x_k, 0, n

        a_n = b_n
        b_n = x_k                           # set new intervals

        if n != 1:
            err = abs(y_old - y_n)
            if err < err_accepted:
                if not giveIterations:
                    return _calcX_k(function, a_n, b_n), err
                if giveIterations:
                    return _calcX_k(function, a_n, b_n), err
        y_old = y_n

    print("Maximum iteration count reached. Break loop and return current values.")
    if not giveIterations:
        return _calcX_k(function, a_n, b_n), err
    if giveIterations:
        return _calcX_k(function, a_n, b_n), err, n


def _calcX_k(function, a_n, b_n):
    return (a_n*function(b_n) - b_n*function(a_n)) / (function(b_n) - function(a_n))


print(secant(f, 1, 2))
