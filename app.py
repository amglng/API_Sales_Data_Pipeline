import csv
import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TICKERS = os.getenv("TICKERS").split(",")

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

def extract(ticker):
    url = f"{BASE_URL}/{ticker}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Extracted data for {ticker}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to extract data for {ticker}: {e}")
        return None


def transform(json_data):
    if not json_data:
        return []

    transformed = []
    symbol = json_data.get("symbol", "UNKNOWN")
    stock_data = json_data.get("data", [])

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

    logging.info(f"Transformed {len(transformed)} rows for {symbol}")
    return transformed


def load(rows, ticker):
    if not rows:
        logging.warning(f"No rows to load for {ticker}")
        return

    os.makedirs("data", exist_ok=True)
    output_file = f"data/{ticker}_data.csv"

    with open(output_file, "w", newline="") as f:
        fieldnames = ["symbol", "date", "open", "high", "low", "close", "volume"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    logging.info(f"Loaded data into {output_file}")

def main():
    for ticker in TICKERS:
        logging.info(f"Processing {ticker}")

        json_data = extract(ticker)
        rows = transform(json_data)
        load(rows, ticker)

    logging.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()