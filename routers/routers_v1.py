import json
from fastapi import APIRouter
from models.models_v1 import SummaryPayload

router = APIRouter(
    prefix="/summarize",
)

@router.post("/", response_model=SummaryPayload)
async def summarize(item: SummaryPayload):
    return SummaryPayload(body=f"Summary of: {item.body}")