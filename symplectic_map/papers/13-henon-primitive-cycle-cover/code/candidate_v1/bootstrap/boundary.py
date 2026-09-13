"""Phase boundary around a single future scientific callable."""


class ScienceBoundary:
    """One-call state machine used by each registered child wrapper."""

    __slots__ = ("phase", "science_call_count")

    def __init__(self):
        self.phase = "CREATED"
        self.science_call_count = 0

    def capability_verified(self):
        if self.phase != "CREATED":
            raise RuntimeError("capability phase order")
        self.phase = "CAPABILITY_VERIFIED"

    def invoke(self, callable_object, *arguments):
        if self.phase != "CAPABILITY_VERIFIED":
            raise RuntimeError("science may run only after capability verification")
        if self.science_call_count != 0:
            raise RuntimeError("science callable is one-shot")
        self.phase = "SCIENCE_ENTERED"
        self.science_call_count = 1
        try:
            value = callable_object(*arguments)
        except BaseException:
            self.phase = "SCIENCE_FAILED"
            raise
        self.phase = "SCIENCE_RETURNED"
        return value

    def output_validated(self):
        if self.phase != "SCIENCE_RETURNED" or self.science_call_count != 1:
            raise RuntimeError("output validation phase order")
        self.phase = "OUTPUT_VALIDATED"

