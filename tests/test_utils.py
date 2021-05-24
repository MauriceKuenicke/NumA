def test_isAxialSymmetricY():
    from numa import utils

    def f(x): return x**2

    assert utils.isAxialSymmetricY(f, 2)


def test_isNotAxialSymmetricY():
    from numa import utils

    def f(x): return x + 4

    assert not utils.isAxialSymmetricY(f, 2)
