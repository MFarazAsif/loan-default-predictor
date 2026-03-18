import sqlite3
import pandas as pd

def create_connection():
    conn = sqlite3.connect('data/loans.db')
    return conn

def load_data_to_db():
    conn = create_connection()
    df = pd.read_csv('data/clean_loan_data.csv')
    df.to_sql('loans', conn, if_exists='replace', index=False)
    print(f"Loaded {len(df)} records into database")
    conn.close()

def run_query(query):
    conn = create_connection()
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

if __name__ == "__main__":
    load_data_to_db()
    print("Database created successfully")