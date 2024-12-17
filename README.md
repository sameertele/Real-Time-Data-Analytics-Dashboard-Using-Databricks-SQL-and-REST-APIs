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

```mermaid
flowchart TD
    User -->|Input| Streamlit Dashboard
    Streamlit Dashboard -->|API Call| Databricks REST API
    Databricks REST API -->|Execute SQL| Databricks SQL
    Databricks SQL -->|Return Data| REST API
    REST API -->|JSON Response| Streamlit Dashboard
    Streamlit Dashboard -->|Visualize| Plotly
```

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
