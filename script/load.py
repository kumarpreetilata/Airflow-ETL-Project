import pandas as pd
import sqlite3
import sys

def load(input_path, db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(input_path)
    df.to_sql("customer_sales", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into SQLite table 'customer_sales'")

if __name__ == "__main__":
    load(sys.argv[1], sys.argv[2])
