"""
in this file i write the db connection file
"""
from sqlalchemy import create_engine

def db_connection():
    """
    this function return a db connection
    """
    engine = create_engine("postgresql://user:password@db:5432/transactions")
    return engine
