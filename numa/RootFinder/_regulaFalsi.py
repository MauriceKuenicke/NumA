from numa import utils


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
        Information whether the value for iterations needed and the error should be returned or not. Lists starts at iteration two
        since the error is always calculated with respect to the previous guess.

    Returns
    -------
    tuple
        (root value, error, convergence)

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
    convergence = list()
    for n in range(1, max_iterations + 1):
        x_k = _calcX_k(function, a_n, b_n)  # Crossing point
        y_n = function(x_k)  # Function value at crossing point
        if function(a_n) * y_n < 0:  # root is on left side of x_k
            b_n = x_k  # set new interval end

            err = abs(function(x_k) - 0)
            convergence.append((n, err))
            if err < err_accepted:
                if not giveIterations:
                    return _calcX_k(function, a_n, b_n), err
                if giveIterations:
                    return _calcX_k(function, a_n, b_n), err, convergence

        elif function(b_n) * y_n < 0:  # root is on right side of x_k
            a_n = x_k  # set new interval start

            err = abs(function(x_k) - 0)
            convergence.append((n, err))
            if err < err_accepted:
                if not giveIterations:
                    return _calcX_k(function, a_n, b_n), err
                if giveIterations:
                    return _calcX_k(function, a_n, b_n), err, convergence

        elif y_n == 0:  # Exact solution
            if not giveIterations:
                return x_k, 0
            if giveIterations:
                convergence.append((n, 0))
                return x_k, 0, convergence
        else:
            utils.MethodStuckError(
                "Regula Falsi won't converge to root. Please adjust limits."
            )
    raise utils.MaximumIterationError(n)


def _calcX_k(function, a_n, b_n):
    return (a_n * function(b_n) - b_n * function(a_n)) / (function(b_n) - function(a_n))
