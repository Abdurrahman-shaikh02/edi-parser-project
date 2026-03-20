import re

def is_valid_npi(npi: str):
    """
    NPI should be 10-digit numeric
    """
    return bool(re.fullmatch(r"\d{10}", npi))


def is_not_empty(value: str):
    return value is not None and value.strip() != ""
