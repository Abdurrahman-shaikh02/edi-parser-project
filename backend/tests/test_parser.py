from app.parser.edi_parser import EDIParser
from app.services.detection import detect_transaction_type
from app.validator.rule_engine import validate_segments

with open("tests/sample-data/sample_835.edi", "r") as f:
    content = f.read()

parser = EDIParser()
segments = parser.parse(content)

print("=== DETECTION ===")
print(detect_transaction_type(segments))

print("\n=== VALIDATION ===")
errors = validate_segments(segments)

for err in errors:
    print(err.to_dict())
