from enum import Enum

class Extension(str, Enum):
    csv = 'csv'
    parquet = 'parquet'
    