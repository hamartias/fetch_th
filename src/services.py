from math import ceil
from uuid import uuid4

_receipts = {}

def process_receipt(receipt_data):
    receipt_id = str(uuid4())
    _receipts[receipt_id] = receipt_data
    return receipt_id

def get_points(receipt_id):
    receipt = _receipts.get(receipt_id)
    if not receipt:
        return None
    points = calculate_points(receipt)
    return points

def calculate_points(receipt):
    points = 0
    points += sum(1 for char in receipt['retailer'] if char.isalpha())
    points += 50 if float(receipt['total'])*100 % 100 == 0 else 0
    points += 25 if float(receipt['total']) * 100 % 25 == 0 else 0
    points += 5 * len(receipt['items']) // 2
    for item in receipt['items']:
        sd = item['shortDescription'].strip()
        if len(sd) % 3 == 0:
            points += int(float(item['price']) * 0.2)
    points += 6 if int(receipt['purchaseDate'].split('-')[2]) % 2 == 1 else 0
    time_as_int = int(receipt['purchaseTime'].replace(':', ''))
    if time_as_int >= 1400 and time_as_int <= 1600:
        points += 10
    return points

