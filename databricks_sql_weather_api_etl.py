# Import necessary libraries
import requests
import pandas as pd
import datetime
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from sqlalchemy import create_engine

# 1. Initialize Spark Session
spark = SparkSession.builder \
    .appName("Databricks SQL Integration with REST API") \
    .config("spark.sql.catalogImplementation", "hive") \
    .getOrCreate()

# 2. Define the REST API details
API_KEY = "openweather_api_key"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITIES = ["Austin", "Houston", "Dallas", "San Antonio", "Fort Worth"] 

# 3. Function to fetch weather data
def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}, Status Code: {response.status_code}")
        return None

# 4. Extract Weather Data from API
weather_data_list = []
for city in CITIES:
    data = fetch_weather_data(city)
    if data:
        weather_data_list.append({
            "City": city,
            "Temperature": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"],
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

# 5. Load Data into a Pandas DataFrame
if weather_data_list:
    weather_df = pd.DataFrame(weather_data_list)
    print("Fetched Weather Data:")
    print(weather_df)

# 6. Save the Pandas DataFrame as a Spark DataFrame
spark_weather_df: DataFrame = spark.createDataFrame(weather_df)

# 7. Write Data to Databricks SQL Table
DB_USER = "your_username"  
DB_PASS = "your_password"  
DB_HOST = "your_databricks_host"  
DB_NAME = "weather_db"

# Create JDBC connection URL
JDBC_URL = f"jdbc:databricks://{DB_HOST}:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/your_workspace_id"

# Write data to Databricks SQL table
TABLE_NAME = "weather_data"

try:
    # Using SQLAlchemy for integration
    engine = create_engine(f"{JDBC_URL};UID={DB_USER};PWD={DB_PASS}", echo=False)

    # Write DataFrame to Databricks SQL table
    weather_df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
    print(f"Data successfully written to Databricks SQL table: {TABLE_NAME}")

except Exception as e:
    print("Error occurred while writing to Databricks SQL:", e)

# 8. Query the Databricks Table for Validation
try:
    query = f"SELECT * FROM {TABLE_NAME}"
    spark.sql(f"REFRESH TABLE {TABLE_NAME}")
    result = spark.read.format("jdbc") \
        .option("url", JDBC_URL) \
        .option("dbtable", f"{DB_NAME}.{TABLE_NAME}") \
        .option("user", DB_USER) \
        .option("password", DB_PASS) \
        .load()

    print("Queried Data from Databricks SQL:")
    result.show()

except Exception as e:
    print("Error querying the table:", e)

# 9. Stop the Spark Session
spark.stop()
