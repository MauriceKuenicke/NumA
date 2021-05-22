
def test_preAnalysis1D():
    import numpy
    from numa import RootFinder
    tol = 1e-3

    def f1(x): return x**2 - 5*x + 3
    def f2(x): return x**2 + 5
    def f3(x): return numpy.sin(2*x) + numpy.e**x

    l1 = RootFinder.preAnalysis1D(f1, 0, 10)
    l1_analytical = [0.697224362, 4.302775637]
    assert numpy.allclose(l1, l1_analytical, atol=tol), \
        "Rootfinder.preAnalysis1D does not agree with known solution"

    l2 = RootFinder.preAnalysis1D(f2, 0, 10)
    assert l2 is None, \
        "Rootfinder.preAnalysis1D does not agree with known solution"

    l3 = RootFinder.preAnalysis1D(f3, -8, 8)
    l3_analytical = [-7.85378749468123572023304286, -6.28411815846958628751033058, -4.70787696145673611503249531,
                     -3.16275351100009246077497969, -1.45273793491168637227001451, -0.377632842071276949433377176]
    assert numpy.allclose(l3, l3_analytical, atol=tol), \
        "Rootfinder.preAnalysis1D does not agree with known solution"

    return None


def test_bisection():
    import numpy
    import math
    from numa import RootFinder
    tol = 1e-14

    def f1(x): return x**2 - 5*x + 3
    def f2(x): return numpy.sin(2*x) + numpy.e**x

    root, error = RootFinder.bisection(f1, 0, 2.5)
    analytical_solution = 0.69722436226800535
    assert math.fabs(root - analytical_solution) < tol and error < tol, \
        "Rootfinder.bisection does not agree with known solution"

    root, error = RootFinder.bisection(f2, -2, -1)
    analytical_solution = -1.45273793491169
    assert math.fabs(root - analytical_solution) < tol and error < tol, \
        "Rootfinder.bisection does not agree with known solution"


def test_bisection_maxIteration():
    import numpy
    from numa import RootFinder, Errors
    import pytest

    def f1(x): return numpy.sin(2*x) + numpy.e**x
    with pytest.raises(Errors.MaximumIterationError):
        root, error = RootFinder.bisection(f1, -2, -1, max_iterations=3)
    return None


def test_bisection_returnIterations():
    import numpy
    from numa import RootFinder
    import math
    tol = 1e-14

    def f1(x): return x*numpy.e**(-x)
    root, error, iterations = RootFinder.bisection(
        f1, -1, 2, giveIterations=True)
    analytical_solution = 0.0
    assert math.fabs(root - analytical_solution) < tol and error < tol and isinstance(iterations, int), \
        "Rootfinder.bisection does not agree with known solution or the number of iterations is not given back correctly"


def test_NewtonRhapson():
    from numa import RootFinder
    import math
    tol = 1e-14

    def f1(x): return x**3 - 2*x + 2
    def df1(x): return 3*x**2 - 2
    root, error = RootFinder.NewtonRhapson(f1, -1.5, df1)
    solution = -1.7692923542386314
    assert math.fabs(root - solution) < tol and error < tol, \
        "Rootfinder.NewtonRhapson does not agree with known solution"


def test_NewtonRhapson_maxIterations():
    from numa import RootFinder, Errors
    import pytest

    def f1(x): return x**3 - 2*x + 2
    def df1(x): return 3*x**2 - 2

    with pytest.raises(Errors.MaximumIterationError):
        root, error = RootFinder.NewtonRhapson(f1, 0, df1)

    with pytest.raises(Errors.MaximumIterationError):
        root, error = RootFinder.NewtonRhapson(f1, -1.5, df1, max_iterations=3)
    return None


def test_NewtonRhapson_returnIterations():
    import numpy
    from numa import RootFinder
    import math
    tol = 1e-14

    def f1(x): return x*numpy.e**(-x)
    def df1(x): return numpy.e**(-x) - x*(numpy.e**(-x))

    root, error, iterations = RootFinder.NewtonRhapson(
        f1, 0.5, df1, giveIterations=True)
    analytical_solution = 0.0

    assert math.fabs(root - analytical_solution) < tol and error < tol and isinstance(iterations, int), \
        "Rootfinder.NewtonRhapson does not agree with known solution or the number of iterations is not given back correctly"


def test_NewtonRhapson_MethodStuckError():
    import numpy
    from numa import RootFinder, Errors
    import pytest

    def f1(x): return x*numpy.e**(-x)
    def df1(x): return numpy.e**(-x) - x*(numpy.e**(-x))

    with pytest.raises(Errors.MethodStuckError):
        root, error = RootFinder.NewtonRhapson(f1, 1, df1)
    return None
