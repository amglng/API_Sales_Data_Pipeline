# API Sales Data Pipeline

## Project Overview

This mini-project demonstrates a **batch data pipeline** that fetches data from a free API, transforms it into a clean CSV format, and outputs summary statistics.

The pipeline follows the **ETL (Extract, Transform, Load)** pattern:

1. **Extract**: Fetch data from a public API in JSON format.
2. **Transform**: Clean, validate, and flatten the data into a tabular structure.
3. **Load**: Save the clean data to a CSV file for analysis.

This project is designed as a learning exercise in **data engineering fundamentals**.

---

## Tech Stack

- Python 3
- `requests` for API calls
- `csv` for CSV handling
- No external frameworks required

---

## Project Structure

```
api-sales-data-pipeline/
│
├── README.md
├── fetch_api_data.py      # ETL pipeline script
├── api_data.csv           # Output CSV (generated after running the pipeline)
└── reflections.md         # Notes & observations about the project
```

---

## Pipeline Workflow

### 1. Extract

Fetch JSON data from the API:

```python
response = requests.get(API_URL)
data = response.json()
```

### 2. Transform

- Flatten JSON data into a CSV-friendly structure
- Clean data and handle missing or invalid entries

### 3. Load

Save the transformed data to `api_data.csv`:

```python
with open("api_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

---

## Example Output

| symbol | date       | open  | high  | low   | close | volume |
|--------|------------|-------|-------|-------|-------|--------|
| FUN    | 2026-02-14 | 18.73 | 19.01 | 18.50 | 18.95 | 10234  |
| FUN    | 2026-02-13 | 18.60 | 18.90 | 18.50 | 18.72 | 8734   |

---

## Learning Outcomes

By completing this project, you will:

- Understand how to extract data from a public API
- Transform nested JSON data into a clean tabular format
- Load the data into a CSV file
- Apply ETL principles in a mini-batch pipeline
- Prepare data for analysis or further processing

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/api-sales-data-pipeline.git
cd api-sales-data-pipeline
```

2. Install required dependencies:
```bash
pip install requests
```

---

## Usage

Run the pipeline:

```bash
python fetch_api_data.py
```

The script will:
1. Fetch data from the API
2. Transform and clean the data
3. Output the results to `api_data.csv`

---

## Requirements

- Python 3.6+
- `requests` library

---

## Future Enhancements

- Add error handling for API failures
- Implement retry logic for failed requests
- Add data validation tests
- Schedule the pipeline to run automatically
- Store data in a SQL database instead of CSV

---

## License

This project is for educational purposes.

---

## Author

Amogelang Ngene
