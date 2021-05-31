
def test_det():
    import numpy as np
    from numa import utils
    tol = 1e-14

    A = np.array([[0, 2, 1], [1, 1, 1], [4, 0, 2]], dtype=float)
    assert np.allclose(
        utils.det(A), 0., atol=tol), "utils.det does not agree with known solution."

    A = np.array([[0, 1, 2], [3, 2, 1], [1, 1, 0]], dtype=float)
    assert np.allclose(
        utils.det(A), 3., atol=tol), "utils.det does not agree with known solution."

    A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
    assert np.allclose(
        utils.det(A), 1., atol=tol), "utils.det does not agree with known solution."


def test_isSingular():
    import numpy as np
    from numa import utils

    A = np.array([[0, 2, 1], [1, 1, 1], [4, 0, 2]], dtype=float)
    assert utils.isSingular(A)

    A = np.array([[7, -1, 0], [4, 6, -3], [-2, 6, 1]], dtype=float)
    assert not utils.isSingular(A)


def test_inverse():
    import numpy as np
    from numa import utils
    tol = 1e-14

    A = np.array([[2, 1], [6, 4]], dtype=float)
    inverseA = np.array([[2, -0.5], [-3, 1]], dtype=float)

    assert np.allclose(utils.inverse(
        A), inverseA, atol=tol), "utils.inverse does not agree with known solution."

    A = np.array([[3, 2, 5], [1, 1, 3], [2, 4, 6]], dtype=float)
    inverseA = np.linalg.inv(A)

    assert np.allclose(utils.inverse(
        A), inverseA, atol=tol), "utils.inverse does not agree with known solution."
