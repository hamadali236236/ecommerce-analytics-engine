import pandas as pd
import numpy as np

def run_cleaning_pipeline():
    try:
        df = pd.read_csv("raw_transactions.csv")
    except FileNotFoundError:
        print("❌ Error: raw_transactions.csv not found. Run data_generator.py first.")
        return

    print("🧹 Cleaning data pipeline...")
    
    # Clean prices
    df['UnitPrice'] = df['UnitPrice'].astype(str).str.replace('$', '', regex=False)
    df['UnitPrice'] = df['UnitPrice'].astype(str).str.replace('USD', '', regex=False)
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
    
    # Filter anomalies
    df = df[(df['UnitPrice'] > 0) & (df['Quantity'] > 0)]
    
    # Normalize text fields
    df['Description'] = df['Description'].str.strip().str.title()
    df['CustomerID'] = df['CustomerID'].fillna(99999).astype(int)
    
    # Feature Engineering
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['HourOfDay'] = df['InvoiceDate'].dt.hour
    
    df.to_csv("clean_transactions.csv", index=False)
    print("✅ Created clean_transactions.csv with metrics!")

if __name__ == "__main__":
    run_cleaning_pipeline()