## Установка

1. Клонируйте репозиторий
2. Установите виртуальное окружение и зависимости

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt



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
    - Source address
    - Destination address
    - Package weight, dimensions and quantity of respective packages
    
    [test_machool_order_data.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/40973bcc-1512-4b5e-b410-6b47012a5eeb/bc65a00c-1c00-497f-b318-17288c202364/test_machool_order_data.json)
    
- A Postman collection, that has of the requests used in this assignment with the same data/credentials.
    
    [Machool (Sandbox) - B360 Test Assignment.postman_collection.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/40973bcc-1512-4b5e-b410-6b47012a5eeb/348bfcc9-299b-41a3-908c-300320925d91/Machool_(Sandbox)_-_B360_Test_Assignment.postman_collection.json)
    

## The Goal

The main goal of the assignment is to write a CLI (Command Line Interface) that allows creating a shipment using Machool’s Sandbox API by going through multiple steps:

1. Program takes the JSON sample file and credentials as an input
2. Program invokes an API Client class object which takes the specified credentials and has its interface tied to the requests it can make
    
    ```jsx
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
    
    ```jsx
    python cli.py create_shipment -f test_machool_order_data.json -keyid <KEY-ID> -api-key <API-KEY>
    ```
    
    The file/command naming is up to your preference, just make it sensible and easy to recognize/use.