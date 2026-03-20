class ValidationError:
    def __init__(self, segment, message, severity="ERROR"):
        self.segment = segment
        self.message = message
        self.severity = severity

    def to_dict(self):
        return {
            "segment": self.segment,
            "message": self.message,
            "severity": self.severity
        }
