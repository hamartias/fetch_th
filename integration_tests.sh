response1=$(curl -X POST "http://localhost:8000/receipts/process" \
  -H "Content-Type: application/json" \
  -d '{
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
}')

response2=$(curl -X POST "http://localhost:8000/receipts/process" \
  -H "Content-Type: application/json" \
  -d '{
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
}')

id1=$(echo "$response1" | sed -n 's/.*"id":"\([^"]*\)".*/\1/p')
id2=$(echo "$response2" | sed -n 's/.*"id":"\([^"]*\)".*/\1/p')

curl -X GET "http://localhost:8000/receipts/$id1/points"
curl -X GET "http://localhost:8000/receipts/$id2/points"
