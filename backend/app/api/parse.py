from fastapi import APIRouter, UploadFile, File
from app.parser.edi_parser import EDIParser
from app.services.detection import detect_transaction_type
from app.validator.rule_engine import validate_segments
from app.services.fix_engine import apply_fixes

router = APIRouter()

@router.post("/parse")
async def parse_edi(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")

    parser = EDIParser()
    segments = parser.parse(content)

    detection = detect_transaction_type(segments)
    errors = validate_segments(segments)
    fixes = apply_fixes(errors)

    return {
        "segments": [s.to_dict() for s in segments],
        "detection": detection,
        "errors": [e.to_dict() for e in errors],
        "fixes": fixes
    }
