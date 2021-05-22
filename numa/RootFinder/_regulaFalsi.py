

def regulaFalsi(function, interval_start, interval_end, max_iterations=10000, giveIterations=False):
    """Approximate one root of a given one-parameter function using the Regula Falsi method;
note that the root has to be inside the interval or the method won't yield any results.
This method can only return one of the possible roots if multiple exist and is generally not used due to it's
unstable nature.


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
Calculates the next upper limit for the interval as

.. math::

    x_k = \\frac{af(b) - bf(a)}{f(b)-f(a)} \\Longrightarrow [a_n, x_k] \\quad \\text{or} \\quad [x_k, b_n]

but chooses the next interval based on the position of x_k.

"""
    err_accepted = 10e-15
    a_n = interval_start
    b_n = interval_end
    for n in range(1, max_iterations+1):
        x_k = _calcX_k(function, a_n, b_n)   # Crossing point
        y_n = function(x_k)                  # Function value at crossing point
        if function(a_n)*y_n < 0:            # root is on left side of x_k
            b_n = x_k                        # set new interval end

            if n != 1:
                err = abs(y_old - y_n)
                if err < err_accepted:
                    if not giveIterations:
                        return _calcX_k(function, a_n, b_n), err
                    if giveIterations:
                        return _calcX_k(function, a_n, b_n), err, n
            y_old = y_n

        elif function(b_n)*y_n < 0:           # root is on right side of x_k
            a_n = x_k                         # set new interval start

            if n != 1:
                err = abs(y_old - y_n)
                if err < err_accepted:
                    if not giveIterations:
                        return _calcX_k(function, a_n, b_n), err
                    if giveIterations:
                        return _calcX_k(function, a_n, b_n), err, n
            y_old = y_n

        elif y_n == 0:        # Exact solution
            if not giveIterations:
                return x_k, 0
            if giveIterations:
                return x_k, 0, n
        else:
            print("Regula Falsi can't find any roots")
            return None
    print("Maximum iteration count reached. Break loop and return current values.")
    if not giveIterations:
        return _calcX_k(function, a_n, b_n), err
    if giveIterations:
        return _calcX_k(function, a_n, b_n), err, n


def _calcX_k(function, a_n, b_n):
    return (a_n*function(b_n) - b_n*function(a_n)) / (function(b_n) - function(a_n))
