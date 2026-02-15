import csv
import requests

API_URL = "https://pocketportfolio.app/api/tickers/FUN/json"

def extract():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # checks for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
        return {}

#transforming the data
def transform(json_data): # Flatten JSON into a list of rows
    transformed = []

    stock_data = json_data.get("data", [])
    symbol = json_data.get("symbol", "UNKNOWN")

    # if "history_sample" in json_data:
    for row in stock_data:
        transformed.append({
            "symbol": symbol,
            "date": row["date"],
            "open": row["open"],
            "high": row["high"],
            "low": row["low"],
            "close": row["close"],
            "volume": row["volume"]
        })

    return transformed
    # print(rows)
    # return rows

    # print(rows)
def load(rows):
    with open("api_data.csv", "w", newline= "") as f:
        fieldnames = ["symbol", "date", "open", "high", "low", "close", "volume"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    print("Data saved to api_data.csv, load stage complete...")

def main():
    json_data = extract()
    rows = transform(json_data)
    load(rows)

if __name__ == "__main__":
    main()




