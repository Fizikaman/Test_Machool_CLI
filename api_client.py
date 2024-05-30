import requests
from config import API_BASE_URL, HEADERS

class APIClient:
    def __init__(self, base_url=API_BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers

    def get_rates(self, shipment_data):
        url = f'{self.base_url}/api/v1/rates'
        response = requests.post(url, headers=self.headers, json=shipment_data)
        response.raise_for_status()
        return response.json()

    def create_shipment(self, shipment_data):
        url = f'{self.base_url}/api/v1/shipments'
        response = requests.post(url, headers=self.headers, json=shipment_data)
        response.raise_for_status()
        return response.json()