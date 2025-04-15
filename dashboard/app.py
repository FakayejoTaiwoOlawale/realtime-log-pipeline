import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["logdb"]
collection = db["logs"]

st.set_page_config(page_title="Real-Time Log Dashboard", layout="wide")
st.title("📊 Real-Time Log Dashboard")

# Filter controls
log_levels = st.multiselect("Select log levels", ["INFO", "WARNING", "ERROR"], default=["INFO", "WARNING", "ERROR"])
services = st.multiselect("Select services", ["auth-service", "payment-service", "order-service"], default=["auth-service", "payment-service", "order-service"])

# Fetch logs from MongoDB
query = {
    "level": {"$in": log_levels},
    "service": {"$in": services}
}

logs = list(collection.find(query).sort("timestamp", -1).limit(100))  # show latest 100 logs in descending order

# Convert logs to DataFrame
#this will run if there is or are logs
if logs:
    df = pd.DataFrame(logs)
    # this is to remove the id column
    df = df.drop(columns=["_id"])
    st.dataframe(df)
else:
    st.info("No logs to display.")
