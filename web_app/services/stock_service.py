# web_app/services/stocks_service.py

import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("")
stock_symbol = "TSLA"
# stock_symbol =input("please select as tock symbol like TSLA")

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}"
print(request_url)

response = requests.get(request_url)
print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
# print(type(response.text)) #> <class 'str'> # not very useful

parsed_response = json.loads(response.text)
print(type(parsed_response)) #> <class 'dict'>

latest_close = parsed_response["Time Series (Daily)"]["2020-02-25"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)