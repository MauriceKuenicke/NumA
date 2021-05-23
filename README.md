# NumA
![](https://numa.readthedocs.io/en/latest/_images/NumA-logo.png)

NumA is a personal Python package storing various useful methods for numerical calculations. This is mostly for the sake of learning and is not intended for high-performance simulations.

[![Test NumA](https://github.com/MauriceKuenicke/NumA/actions/workflows/test_package.yml/badge.svg)](https://github.com/MauriceKuenicke/NumA/actions/workflows/test_package.yml)  [![codecov](https://codecov.io/gh/MauriceKuenicke/NumA/branch/main/graph/badge.svg?token=X39JFT8UEG)](https://codecov.io/gh/MauriceKuenicke/NumA)  [![Documentation Status](https://readthedocs.org/projects/numa/badge/?version=latest)](https://numa.readthedocs.io/en/latest/?badge=latest)

-----------------------------------------------

Find NumA's latest documentation [here](https://numa.readthedocs.io/en/latest/).

## Installation
``NumA`` is in early development and currently not yet available on PyPI, but it can be
installed by downloading the source code or cloning the GitHub
repository and running the standard::

       python setup.py install

command or its usual variants (``python setup.py install --user``,
``python setup.py install --prefix=/PATH/TO/INSTALL/DIRECTORY``,
etc.).

## Intro
``NumA`` is a Python package that contains some very useful
functions for numerical analysis. As an example, we can approximate the root of a given function
using the Bisection method. As an example, we can calculate the root for f(x) = 3x-3 on the interval [-3,5]

       >>> import numa
       >>> f = lambda x: 3*x-3
       >>> numa.RootFinder.bisection(f, -3, 5)
       # (1.0, 0)

Similarly, we can do a basic 1D pre analysis in [-100,100] of possible root values to help define needed interval limits

       >>> f = lambda x: x**2 - 5*x +3
       >>> numa.RootFinder.preAnalysis1D(f, -100, 100)
       # [0.6990069900698899,4.3030430304303025]


``NumA`` also includes simple methods for integrating a function,
in the ``numa.integrate`` submodule. This submodule contains methods
like ``riemann`` and  ``newton_cotes`` that approximate the integral of any
one-parameter function. Other methods will follow.
