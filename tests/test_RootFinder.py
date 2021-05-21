
def test_preAnalysis1D():
    # Direct test that the square works based on known solutions
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
