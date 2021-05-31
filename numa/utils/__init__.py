
class MaximumIterationError(Exception):
    """Exception raised when the maximum number of iterations is reached.

    Attributes:
        iterations -- input salary which caused the error
    """

    def __init__(self, iterations):
        self.iterations = iterations
        self.message = f"Maxmimum number of {self.iterations} iterations reached"
        super().__init__(self.message)


class MethodStuckError(Exception):
    """Exception raised when a method is stuck. E.g. a zero-derivative during the Newton-Rhapson-Method.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, reason):
        self.reason = reason
        self.message = f"Method is stuck. Reason given: {self.reason}"
        super().__init__(self.message)


class DimensionError(Exception):
    """Exception raised when the dimension numbers don't match.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, reason):
        self.reason = reason
        self.message = f"{self.reason}"
        super().__init__(self.message)


def _checkDimensions(A, b):
    if not A.shape[0] == A.shape[1]:
        raise DimensionError("Input matrix A is not quadratic!")
    if not b.shape[0] == A.shape[1]:
        raise DimensionError("Dimensions of A and b do not match!")
