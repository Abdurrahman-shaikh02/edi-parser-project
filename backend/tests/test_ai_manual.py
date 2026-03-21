from app.ai.ai_service import explain_errors

# fake error (simulate your validator output)
errors = [
    {
        "segment": "NM1",
        "message": "Invalid NPI: INVALID_NPI",
        "suggestion": "NPI should be a 10-digit numeric value"
    }
]

result = explain_errors(errors)

for r in result:
    print("\n=== AI OUTPUT ===")
    print("Error:", r["message"])
    print("Suggestion:", r["suggestion"])
    print("AI Explanation:", r["ai_explanation"])
