import json
from fastapi import APIRouter
from models.models_v1 import SummaryResponse, SummaryRequest
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model directly on startup
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

router = APIRouter(
    prefix="/summarize",
)

@router.post("/", response_model=SummaryResponse)
async def summarize(request: SummaryRequest):
    # Tokenize input for BART
    inputs = tokenizer(request.text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Generate summary
    outputs = model.generate(
        inputs["input_ids"],
        max_length=142,  # CNN/DM dataset standard
        min_length=56,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    
    # Decode the summary
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return SummaryResponse(
        summary=summary,
        original_length=len(request.text),
        summary_length=len(summary)
    )