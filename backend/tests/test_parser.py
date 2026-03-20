from app.parser.edi_parser import EDIParser
from app.services.detection import detect_transaction_type

with open("tests/sample-data/sample_835.edi", "r") as f:
    content = f.read()

parser = EDIParser()
segments = parser.parse(content)

result = detect_transaction_type(segments)

print("\n=== DETECTION ===")
print(result)
