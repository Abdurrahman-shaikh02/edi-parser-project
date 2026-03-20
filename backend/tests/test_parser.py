from app.parser.edi_parser import EDIParser

with open("tests/sample-data/valid_837.edi", "r") as f:
    content = f.read()

parser = EDIParser()
segments = parser.parse(content)

for seg in segments:
    print(seg, end="\n")
