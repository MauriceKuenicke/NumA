from ._symmetry import *


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


class SymmetryError(Exception):
    """Exception raised when a function doesn't meet some symmetry property.

    Attributes:
        symmetry -- what symmetry is not met
    """

    def __init__(self, symmetry):
        self.symmetry = symmetry
        self.message = f"Input function not valid. {self.symmetry}"
        super().__init__(self.message)
