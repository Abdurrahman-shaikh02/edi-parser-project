def suggest_fix(error):
    """
    Generate fix suggestions based on error message
    """

    msg = error.message.lower()

    # 🔹 NPI fix
    if "invalid npi" in msg:
        return "NPI should be a 10-digit numeric value (e.g., 1234567890)"

    # 🔹 NM1 missing elements
    if "nm1 segment has too few elements" in msg:
        return "Ensure NM1 has required fields: entity type, name, identifier"

    # 🔹 Missing claim ID
    if "missing claim id" in msg:
        return "CLM segment must include a valid claim ID (first element)"

    return "Check segment format as per EDI standard"


def apply_fixes(errors):
    """
    Attach suggestions to each validation error
    """

    enriched = []

    for err in errors:
        enriched.append({
            "segment": err.segment,
            "message": err.message,
            "severity": err.severity,
            "suggestion": suggest_fix(err)
        })

    return enriched
