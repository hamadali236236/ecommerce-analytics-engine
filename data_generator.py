import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_messy_ecommerce_data(records=5000):
    np.random.seed(42)
    base_date = datetime(2026, 1, 1)
    user_ids = [int(x) for x in np.random.randint(10000, 10500, size=records)]
    
    products = {
        'PROD001': ('Himalayan Pink Salt Lamp', 25.00, 'Home Decor'),
        'PROD002': ('Organic Pink Salt Fine Grain 1kg', 8.50, 'Grocery'),
        'PROD003': ('Coarse Rock Salt 5kg Bag', 18.00, 'Grocery'),
        'PROD004': ('Premium Salt Cooking Block', 45.00, 'Kitchenware'),
        'PROD005': ('Ceramic Salt Grinder', 15.00, 'Kitchenware')
    }
    
    prod_codes = list(products.keys())
    chosen_codes = np.random.choice(prod_codes, size=records, p=[0.3, 0.3, 0.2, 0.1, 0.1])
    
    data = []
    for i in range(records):
        p_code = chosen_codes[i]
        p_name, p_price, p_cat = products[p_code]
        
        raw_price = f"${p_price} USD" if np.random.random() > 0.15 else f" {p_price}   "
        if np.random.random() < 0.02: 
            raw_price = "-$10.00"
            
        cust_id = user_ids[i] if np.random.random() > 0.10 else np.nan
        desc = p_name if np.random.random() > 0.10 else f"  {p_name.upper()}  "
        quantity = int(np.random.choice([1, 2, 3, 4, 5], p=[0.5, 0.3, 0.1, 0.05, 0.05]))
        
        if raw_price == "-$10.00":
            quantity = 0
            
        days_offset = np.random.randint(0, 180)
        hour_offset = np.random.randint(8, 23)
        timestamp = base_date + timedelta(days=days_offset, hours=hour_offset)
        
        data.append({
            'InvoiceNo': 100000 + i,
            'StockCode': p_code,
            'Description': desc,
            'Quantity': quantity,
            'InvoiceDate': timestamp,
            'UnitPrice': raw_price,
            'CustomerID': cust_id,
            'Category': p_cat
        })
        
    df = pd.DataFrame(data)
    df.to_csv("raw_transactions.csv", index=False)
    print("✅ Created raw_transactions.csv successfully!")

if __name__ == "__main__":
    generate_messy_ecommerce_data()