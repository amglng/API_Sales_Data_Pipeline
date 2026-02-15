import csv
import requests

API_URL = "https://pocketportfolio.app/api/tickers/FUN/json"


#fetching the api data
def extract():
    response = response.get(API_URL)
    return response.json()

#transforming the data
def transform(json_data): # Flatten JSON into a list of rows
    rows = []

    if "history_sample" in json_data:
        for item in json_data["history_sample"]:
            rows.append({
            "symbol": json_data["symbol"],
            "date": item.get("date", ""),
            "open": item.get("open", ""),
            "high": item.get("high", ""),
            "low": item.get("low", ""),
            "close": item.get("close", ""),
            "volume": item.get("volume", "")
        })
    print(rows)
    return rows

    # print(rows)


