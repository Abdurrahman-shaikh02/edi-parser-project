from .prompt_builder import build_prompt
from .llm_client import get_ai_explanation


def explain_errors(errors):
    """
    Add AI explanations to validation errors
    """

    enriched = []

    for err in errors:
        prompt = build_prompt(err)
        explanation = get_ai_explanation(prompt)

        enriched.append({
            "segment": err["segment"],
            "message": err["message"],
            "suggestion": err["suggestion"],
            "ai_explanation": explanation
        })

    return enriched
