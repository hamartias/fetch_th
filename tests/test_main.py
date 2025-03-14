import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

example_one = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}

example_two = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

examples = [example_one, example_two]
expected_points = [28, 109]

def _test_process_receipt(example_receipt_json):
    response = client.post("/receipts/process", json=example_receipt_json)
    assert response.status_code == 200
    assert "id" in response.json()

def _test_get_points(example_receipt_json, expected_points):
    post_response = client.post("/receipts/process", json=example_receipt_json)
    receipt_id = post_response.json()["id"]

    # Then, get points
    get_response = client.get(f"/receipts/{receipt_id}/points")
    assert get_response.status_code == 200
    assert get_response.json()["points"] == expected_points

def test_process_receipt():
    for example in examples:
        _test_process_receipt(example)

def test_get_points():
    for example, expected in zip(examples, expected_points): 
        _test_get_points(example, expected)

def test_get_points_not_found():
    response = client.get("/receipts/nonexistent_id/points")
    assert response.status_code == 404
    assert response.json()["detail"] == "Receipt not found"
