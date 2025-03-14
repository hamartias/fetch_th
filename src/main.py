from fastapi import FastAPI, HTTPException
from .schemas import ReceiptRequest, ReceiptResponse, PointsResponse
from .services import process_receipt, get_points

app = FastAPI()

@app.post("/receipts/process", response_model=ReceiptResponse)
async def process(receipt: ReceiptRequest):
    receipt_id = process_receipt(receipt.dict())
    return ReceiptResponse(id=receipt_id)

@app.get("/receipts/{id}/points", response_model=PointsResponse)
async def points(id: str):
    points = get_points(id)
    if points is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return PointsResponse(id=id, points=points)
