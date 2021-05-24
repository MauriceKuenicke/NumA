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


class MethodNotSupportedError(Exception):
    """Exception raised when a method is not supported.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, method_list):
        self.method_list = ",".join(method_list)
        self.message = f"Input method not allowed. Please choose one of these methods: {self.method_list}."
        super().__init__(self.message)


class MissingParameterError(Exception):
    """Exception raised when parameter are missing.

    Attributes:
        reason -- reason given why the method can't proceed
    """

    def __init__(self, parameter):
        self.parameter_list = ",".join(parameter)
        self.message = f"Missing parameter detected. Please add the following parameter combination: {self.parameter_list}"
        super().__init__(self.message)
