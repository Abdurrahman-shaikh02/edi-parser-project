from .error_model import ValidationError
from .validators import is_valid_npi, is_not_empty


def validate_segments(segments):
    errors = []

    for seg in segments:

        # 🔹 Rule 1: NM1 must have enough elements
        if seg.name == "NM1":
            if len(seg.elements) < 5:
                errors.append(
                    ValidationError(
                        segment="NM1",
                        message="NM1 segment has too few elements"
                    )
                )

        # 🔹 Rule 2: NPI validation (NM1 with XX qualifier)
        if seg.name == "NM1":
            if len(seg.elements) >= 9:
                qualifier = seg.elements[7]
                npi = seg.elements[8]

                if qualifier == "XX" and not is_valid_npi(npi):
                    errors.append(
                        ValidationError(
                            segment="NM1",
                            message=f"Invalid NPI: {npi}"
                        )
                    )

        # 🔹 Rule 3: CLM segment must have claim ID
        if seg.name == "CLM":
            if len(seg.elements) < 1 or not is_not_empty(seg.elements[0]):
                errors.append(
                    ValidationError(
                        segment="CLM",
                        message="Missing Claim ID"
                    )
                )

    return errors
