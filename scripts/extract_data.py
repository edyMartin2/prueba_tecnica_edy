"""
this file read all data from db and return a csv file
"""
import pandas as pd
from db.db import db_connection
import os


def extarct_db():
    """
    here we write the code
    """
    db = db_connection()
    cv_output_path = os.path.join(os.path.dirname(__file__), "data", "extracted_data.csv")
    parquet_output_path = os.path.join(os.path.dirname(__file__), "data", "extracted_data.parquet")
    data_frame = pd.read_sql('SELECT * FROM raw_data', db)
    os.makedirs(os.path.dirname(cv_output_path), exist_ok=True)
    data_frame.to_csv(cv_output_path, index=False)
    data_frame.to_parquet(parquet_output_path, index=False)
    
    return cv_output_path, parquet_output_path
extarct_db()
