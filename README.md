# Real-Time Data Analytics Dashboard Using Databricks SQL and REST APIs

## Project Overview
This project builds a real-time data analytics dashboard by integrating **Databricks SQL** with REST APIs. It automates query execution, retrieves insights, and visualizes the data dynamically using Streamlit and Plotly.

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Project Architecture](#project-architecture)
3. [Features](#features)
4. [Setup Instructions](#setup-instructions)
5. [REST API Details](#rest-api-details)
6. [Sample Code](#sample-code)
7. [Visualization](#visualization)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## Technologies Used
- **Databricks SQL**: For running SQL queries and retrieving analytical results.
- **Databricks REST APIs**: For programmatically executing SQL queries.
- **Python**: Primary language for scripting and API integration.
- **Streamlit**: For building the interactive web-based dashboard.
- **Plotly**: For creating real-time visualizations.
- **JSON**: For handling REST API responses.

---

## Project Architecture


flowchart TD
    User -->|Input| Streamlit Dashboard
    Streamlit Dashboard -->|API Call| Databricks REST API
    Databricks REST API -->|Execute SQL| Databricks SQL
    Databricks SQL -->|Return Data| REST API
    REST API -->|JSON Response| Streamlit Dashboard
    Streamlit Dashboard -->|Visualize| Plotly
    

1. **Streamlit** acts as the frontend for users to input parameters and visualize results.
2. **Databricks REST APIs** interact with Databricks SQL for query execution.
3. The **results** are fetched as JSON responses and processed in Python.
4. The data is visualized using **Plotly** in the dashboard.

---

## Features
- Automates SQL query execution via Databricks REST APIs.
- Fetches and processes query results dynamically.
- Provides an interactive dashboard for querying and visualization.
- Real-time data visualization using Plotly.
- Customizable input parameters for SQL queries.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/databricks-real-time-dashboard.git
   cd databricks-real-time-dashboard
   ```

2. **Create a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate    # For Windows
   ```

3. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Databricks credentials:**
   - Get your **Databricks Workspace URL** and **Access Token** from Databricks.
   - Create a `.env` file in the root directory:
     ```bash
     DATABRICKS_HOST=https://<your-databricks-workspace>
     DATABRICKS_TOKEN=<your-databricks-access-token>
     ```

5. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

6. Open your browser and visit `http://localhost:8501`.

---

## REST API Details
The project uses the **Databricks SQL Execution API**:

### Endpoint
```
POST /api/2.0/sql/statements
```

### Request Payload
```json
{
    "statement": "SELECT * FROM sample_table LIMIT 100",
    "warehouse_id": "<warehouse-id>",
    "catalog": "<catalog-name>",
    "schema": "<schema-name>"
}
```

### Sample Response
```json
{
    "statement_id": "<statement-id>",
    "result": {
        "data_array": [["value1", "value2"], ["value3", "value4"]]
    }
}
```

---

## Sample Code
Here is a snippet demonstrating Databricks SQL API integration:

```python
import requests
import os
import json
from dotenv import load_dotenv

# Load Databricks credentials
load_dotenv()
DATABRICKS_HOST = os.getenv("DATABRICKS_HOST")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

# API Endpoint
url = f"{DATABRICKS_HOST}/api/2.0/sql/statements"
headers = {
    "Authorization": f"Bearer {DATABRICKS_TOKEN}",
    "Content-Type": "application/json"
}

# SQL Statement
payload = {
    "statement": "SELECT * FROM my_table LIMIT 10",
    "warehouse_id": "<warehouse-id>",
    "catalog": "hive_metastore",
    "schema": "default"
}

# Execute SQL
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

---

## Visualization
The Streamlit dashboard visualizes the query output in real-time using Plotly charts:

- **Bar Charts** for category-wise data.
- **Line Charts** for trends and time series.
- **Tables** for raw data display.

---

## Future Enhancements
- Add caching for frequent queries to reduce API calls.
- Include authentication for dashboard access.
- Support multiple query submissions and result comparisons.
- Integrate Databricks Jobs for scheduled query execution.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
