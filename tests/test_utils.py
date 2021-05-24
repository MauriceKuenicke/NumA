def test_isAxialSymmetricY():
    from numa import utils

    def f(x): return x**2

    assert utils.isAxialSymmetricY(f, 2)
