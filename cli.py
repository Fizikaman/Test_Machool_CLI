import json
import os
import requests

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
    rates = client.get_rates(shipment_data)
    print('Rates:', rates)

    # Выбор самого дешевого сервиса
    cheapest_rate = min(rates, key=lambda x: x['totalPrice'])
    shipment_data['serviceId'] = cheapest_rate['serviceId']

    # Создание отправки
    shipment = client.create_shipment(shipment_data)
    print('Shipment:', shipment)

    # Сохранение PDF
    tracking_number = shipment['trackingNumber']
    label_url = shipment['labelUrl']

    label_response = requests.get(label_url)
    label_path = os.path.join(os.path.dirname(file_path), f'{tracking_number}.pdf')
    with open(label_path, 'wb') as f:
        f.write(label_response.content)

    log_path = os.path.join(os.path.dirname(file_path), f'{tracking_number}.log')
    with open(log_path, 'w') as f:
        json.dump(shipment, f, indent=4)