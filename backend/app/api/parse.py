from fastapi import APIRouter, UploadFile, File
from app.parser.edi_parser import EDIParser
from app.services.detection import detect_transaction_type

router = APIRouter(prefix="/parse", tags=["Parse"])


@router.post("/")
async def parse_edi(file: UploadFile = File(...)):
    content = await file.read()
    content = content.decode("utf-8")

    parser = EDIParser()
    segments = parser.parse(content)

    return {
        "segments": [s.to_dict() for s in segments],
        "transaction": detect_transaction_type(segments)
    }
