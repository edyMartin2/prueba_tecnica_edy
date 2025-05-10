"""
    here we dispersion_to_table information
"""
import os
import pandas as pd
from db.db import db_connection
from sqlalchemy import String, Numeric, DateTime


def dispersion_to_table():
    """
    take the last csv generated and upload to db in separate tables
    """
    db = db_connection()
    input_path = os.path.join(os.path.dirname(__file__), "data", "transfrom_data.csv")
    data_frame = pd.read_csv(input_path)
    
    
    companies = data_frame[["company_id", "company_name"]].drop_duplicates().dropna(subset=["company_id", "company_name"])
    charges = data_frame[["id", "company_id", "amount", "transaction_date"]]
    charges[charges['amount'].abs() < 1e10]
    
    companies.to_sql('companies', db, if_exists='replace', index=False)
    
    charges_dtypes = {
        "id": String(64),
        "company_id": String(64),
        "company_name": String(130),
        "amount": String(64),
        "status": String(30),
        "created_at": DateTime(),
        "updated_at": DateTime(),
    }
    
    charges.to_sql('charges', db, if_exists='replace', index=False, dtype=charges_dtypes)
    
dispersion_to_table()