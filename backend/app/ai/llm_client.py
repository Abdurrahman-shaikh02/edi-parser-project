import os
from groq import Groq

# Toggle AI (important for tests)
USE_AI = os.getenv("USE_AI", "true").lower() == "true"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_ai_explanation(prompt: str) -> str:
    """
    Call Groq LLM to get explanation
    """

    if not USE_AI:
        return "AI disabled (mock explanation for testing)."

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful EDI expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI error: {str(e)}"
