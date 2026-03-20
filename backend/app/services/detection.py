def detect_transaction_type(segments):
    """
    Detect EDI transaction type using ST segment
    """

    for seg in segments:
        if seg.name == "ST":
            if not seg.elements:
                return {
                    "code": "UNKNOWN",
                    "description": "Empty ST segment"
                }

            code = seg.elements[0]

            mapping = {
                "837": "Healthcare Claim",
                "835": "Payment / Remittance",
                "834": "Enrollment / Membership"
            }

            return {
                "code": code,
                "description": mapping.get(code, "Unknown transaction type")
            }

    return {
        "code": "UNKNOWN",
        "description": "ST segment not found"
    }
