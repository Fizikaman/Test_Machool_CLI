## Установка

1. Клонируйте репозиторий
2. Установите виртуальное окружение и зависимости

```sh
python -m venv venv
source venv/bin/activate (Для Windows: venv\Scripts\activate)
pip install -r requirements.txt
Для запуска из терминала - python main.py create_shipment -f file_folder/test_machool_order_data.json -keyid bCahFZHQc3 -apikey 645744e8-a047-421a-b882-7d2471f6bab5
```


## Introduction

This assignment will involve working with a sandbox environment of a real courier API - Machool and creating a mock shipment here.

## Supporting information

[Machool - API documentation](https://api.machool.com/external/docs)

Base URL:  [https://api.sandbox.machool.com](https://api.sandbox.machool.com/)

Auth headers:

| x-key-id | bCahFZHQc3 |
| --- | --- |
| x-api-key | 645744e8-a047-421a-b882-7d2471f6bab5 |
- A sample JSON file that contains the mock shipment data, including:

```sh
    - Source address
    - Destination address
    - Package weight, dimensions and quantity of respective packages
```

- A Postman collection, that has of the requests used in this assignment with the same data/credentials.
    

## The Goal

The main goal of the assignment is to write a CLI (Command Line Interface) that allows creating a shipment using Machool’s Sandbox API by going through multiple steps:

1. Program takes the JSON sample file and credentials as an input
2. Program invokes an API Client class object which takes the specified credentials and has its interface tied to the requests it can make
    
```sh
    class APIClient(...):
    		def get_rates(...):
    			  ...
```
    
3. API client sends a POST request to the Rates endpoint ([api/v1/rates/](https://api.machool.com/external/docs#/Rates/RatesController_getRatesV1)) to determine the cheapest carrier service
4. API Client sends a POST request to the Shipments endpoint ([api/v1/shipments](https://api.machool.com/external/docs#/Shipments/ShipmentsController_createShipment)) to create a shipment with the found service
5. Program saves the label received from the shipment creation as a PDF file in the same folder as the JSON sample with the filename of the tracking number of the created shipment (example: 232123512.pdf)
6. Program saves the full request/response data as a .log file in the same folder as the JSON sample (same naming as the PDF file - 232123512.log)

## Important notes

- Make the program usable through a terminal of any regular OS (Windows/OSX/Linux), example:
    
```sh
    python cli.py create_shipment -f test_machool_order_data.json -keyid <KEY-ID> -api-key <API-KEY>
```
    
    The file/command naming is up to your preference, just make it sensible and easy to recognize/use.