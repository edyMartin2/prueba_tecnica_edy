"""
this file read the file csv 
"""
import pandas as pd
from datetime import datetime
import os

def transform_data():
    """
    here i read the file extract from db and transform data
    """
    input_path = os.path.join(os.path.dirname(__file__), "data", "extracted_data.csv")
    data_frame = pd.read_csv(input_path)
    data_frame["transaction_date"] = pd.to_datetime(datetime.now())
    data_frame["amount"] = data_frame["amount"].astype(float)
    data_frame = data_frame.rename(columns={'name': 'company_name'})
    output_path = os.path.join(os.path.dirname(__file__), "data", "transfrom_data.csv")
    data_frame.to_csv(output_path, index=False)
transform_data()
