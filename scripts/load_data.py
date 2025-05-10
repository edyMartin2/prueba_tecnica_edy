"""
this file read a csv and upload information to a db
"""
import pandas as pd
from db.db import db_connection
import pytest
from unittest.mock import patch, MagicMock

def load_data():
    """
    here we read the document and all data
    """
    read_csv = pd.read_csv("./data/data_prueba_tecnica.csv")
    db = db_connection()
    read_csv.to_sql('raw_data', db, if_exists='replace', index=False)

load_data()
