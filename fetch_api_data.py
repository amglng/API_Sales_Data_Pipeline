import csv
import requests

API_URL = "https://pocketportfolio.app/api/tickers/FUN/json"


#fetching the api data
def extract():
    response = response.get(API_URL)
    return response.json()


