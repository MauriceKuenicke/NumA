
def test_conditionNumber():
    import numpy as np
    from numa import LinearSystem
    tol = 1e-14

    A = np.array([[7, -1, 0], [4, 6, -3],
                  [-2, 6, 1]], dtype=float)
    true_value = np.linalg.cond(A, p=2)
    calc_value = LinearSystem.condition(A, p=2)
    assert np.allclose(
        calc_value, true_value, atol=tol), "LinearSystem.condition does not agree with known solution."


def test_Gauss():
    import numpy as np
    from numa import LinearSystem
    tol = 1e-14

    A = np.array([[7, -1, 0], [4, 6, -3],
                  [-2, 6, 1]], dtype=float)
    b = np.array([5, 7, 13], dtype=float)

    true_solution = np.array([1, 2, 3], dtype=float)
    x_calculated = LinearSystem.solveGauss(A, b)

    assert np.allclose(
        x_calculated, true_solution, atol=tol), "LinearSystem.solveGauss does not agree with known solution"


def test_Gauss_wrongDimensions():
    import numpy as np
    from numa import LinearSystem, utils
    import pytest

    A = np.array([[7, -1, 0], [4, 6, -3], [0, 2, 1],
                  [-2, 6, 1]], dtype=float)
    b = np.array([5, 7, 13], dtype=float)

    with pytest.raises(utils.DimensionError):
        x_calculated = LinearSystem.solveGauss(A, b)

    A = np.array([[7, -1, 0], [4, 6, -3],
                  [-2, 6, 1]], dtype=float)
    b = np.array([5, 7, 13, 3], dtype=float)
    with pytest.raises(utils.DimensionError):
        x_calculated = LinearSystem.solveGauss(A, b)
    return None


def test_Gauss_singularMatrix():
    import numpy as np
    from numa import LinearSystem, utils
    import pytest

    A = np.array([[0, 2, 1], [1, 1, 1], [4, 0, 2]], dtype=float)
    b = np.array([1, 1, 1], dtype=float)

    with pytest.raises(utils.SingularityError):
        x = LinearSystem.solveGauss(A, b)


def test_LU():
    import numpy as np
    from numa import LinearSystem
    tol = 1e-14

    A = np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]], dtype=float)
    L, U = LinearSystem.LU(A)
    A_reconstructed = np.matmul(L, U)
    assert np.allclose(
        A_reconstructed, A, atol=tol), "LinearSystem.LU does not agree with known solution"


def test_solveLU():
    import numpy as np
    from numa import LinearSystem
    tol = 1e-14

    A = np.array([[7, -1, 0], [4, 6, -3],
                  [-2, 6, 1]], dtype=float)
    b = np.array([5, 7, 13], dtype=float)
    true_solution = np.array([1, 2, 3], dtype=float)

    x_calculated = LinearSystem.solveLU(A, b)
    assert np.allclose(
        x_calculated, true_solution, atol=tol), "LinearSystem.solveLU does not agree with known solution"


def test_LU_singularMatrix():
    import numpy as np
    from numa import LinearSystem, utils
    import pytest

    A = np.array([[0, 2, 1], [1, 1, 1], [4, 0, 2]], dtype=float)
    b = np.array([1, 1, 1], dtype=float)

    with pytest.raises(utils.SingularityError):
        x = LinearSystem.solveLU(A, b)
