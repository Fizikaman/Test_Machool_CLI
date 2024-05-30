import json
import os
import base64

from api_client import APIClient

def create_shipment(file_path, key_id, api_key):
    with open(file_path, 'r') as f:
        shipment_data = json.load(f)

    # Обнвляем заголовки
    headers = {
        'x-key-id': key_id,
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }

    client = APIClient(headers=headers)
    response = client.get_rates(shipment_data)
    rates = response['rates']

    # Выбор самого дешевого сервиса
    cheapest_rate = min(rates, key=lambda x: x['totalPrice'])
    shipment_data['provider'] = cheapest_rate['provider']
    shipment_data['serviceCode'] = cheapest_rate['serviceCode']
    shipment_data['options'] = cheapest_rate['options']
    shipment_data['getLabel'] = True
    shipment_data['reference'] = "GV000001TEST"
    shipment_data['labelSize'] = "4x6"

    # Создание отправки
    shipment = client.create_shipment(shipment_data)
    tracking_number = shipment['trackingNumber']

    # Сохранение запроса/ответа
    log_file = {'Request data': shipment_data, 'Response data': shipment}
    log_path = os.path.join(os.path.dirname(file_path), f'{tracking_number}.log')
    with open(log_path, 'w') as f:
        json.dump(log_file, f, indent=4)

    # Сохранение PDF
    label_path = os.path.join(os.path.dirname(file_path), f'{tracking_number}.pdf')
    label = shipment['label']
    pdf_data = base64.b64decode(label)
    with open(label_path, 'wb') as f:
       f.write(pdf_data)