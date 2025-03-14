from pydantic import BaseModel

class ReceiptRequest(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[dict]
    total: str

class ReceiptResponse(BaseModel):
    id: str

class PointsResponse(BaseModel):
    id: str
    points: int
