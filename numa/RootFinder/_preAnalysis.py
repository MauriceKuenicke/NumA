import numpy as np


def preAnalysis1D(function, interval_start, interval_end):
    """Approximate possible roots of a given one-parameter function and the given domain.
This function creates a numpy.linspace and calculates all possible values on that domain. The function is assumed
to be continuous in that case. Positions where the sign of the function value changes will be marked as a possible
root area and returned. This method should not be used to approximate roots. It should rather be a tool to further
define the domain space for methods like numa.RootFinder.bisection.


Parameters
----------
function: callable, (e.g f = lambda x: x**2)
    Function to analyze.
interval_start: int
    lower limit of the domain
interval_end: int
    upper limit of the domain

Returns
-------
list
    A list of all x values that are in the near area of a root.

"""
    domain = np.linspace(interval_start, interval_end, 100000)
    f_vals = function(domain)
    sign_switches = list()
    for index in range(1, len(f_vals)):
        if f_vals[index] * f_vals[index-1] < 0:
            sign_switches.append(domain[index])
    if len(sign_switches) == 0:
        return None
    return sign_switches
