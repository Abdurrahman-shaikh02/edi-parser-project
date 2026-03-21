from fastapi import APIRouter, UploadFile, File
from app.parser.edi_parser import EDIParser
from app.validator.rule_engine import validate_segments
from app.services.fix_engine import apply_fixes
from app.ai.ai_service import explain_errors

router = APIRouter(prefix="/validate", tags=["Validation"])


@router.post("/")
async def validate_edi(file: UploadFile = File(...)):
    content = await file.read()
    content = content.decode("utf-8")

    parser = EDIParser()
    segments = parser.parse(content)

    errors = validate_segments(segments)
    fixed = apply_fixes(errors)

    # 🔥 AI layer
    enriched = explain_errors(fixed)

    return {
        "errors": enriched
    }
