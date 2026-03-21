def build_prompt(error):
    """
    Convert validation error into a clean AI prompt
    """

    return f"""
You are an expert in healthcare EDI (X12).

Explain this error in simple terms:

Error: {error['message']}

Your explanation must include:
- What the field means
- Why it is incorrect
- How to fix it

Keep it short (3-4 lines), beginner-friendly.
"""
