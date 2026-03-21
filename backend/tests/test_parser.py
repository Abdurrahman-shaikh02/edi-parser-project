from app.parser.edi_parser import EDIParser
from app.services.detection import detect_transaction_type
from app.validator.rule_engine import validate_segments

with open("tests/sample-data/sample_834.edi", "r") as f:
    content = f.read()

parser = EDIParser()
segments = parser.parse(content)
json_segments = parser.parse_to_json(content)

print("\n=== PARSER ===")
for seg in segments:
    print(seg)


print("\n=== PARSER (JSON) ===")
for seg in json_segments:
    print(seg)

print("\n=== DETECTION ===")
print(detect_transaction_type(segments))

print("\n=== VALIDATION ===")
errors = validate_segments(segments)

for err in errors:
    print(err.to_dict())


from app.services.fix_engine import apply_fixes

errors = validate_segments(segments)
fixed = apply_fixes(errors)

print("\n=== FIX SUGGESTIONS ===")
for f in fixed:
    print(f)





print("\n\n=== AI ===")
from app.services.fix_engine import apply_fixes
from app.validator.rule_engine import validate_segments
from app.ai.ai_service import explain_errors

errors = validate_segments(segments)
fixed = apply_fixes(errors)

ai_output = explain_errors(fixed)

for item in ai_output:
    print(item)
