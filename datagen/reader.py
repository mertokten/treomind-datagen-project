from typing import (
    Literal, 
    List
)

import pandas as pd


def read_source_file(
    file_path: str,
    extension: Literal['csv', 'parquet'] = 'csv',
    sep: str = ',',
    excluded_cols: List[str] = []
):
    if extension == 'csv':
        df = pd.read_csv(file_path, sep=sep)
    elif extension == 'parquet':
        df = pd.read_parquet(file_path, engine='auto')
    else:
        raise ValueError("Desteklenmeyen dosya türü: csv veya parquet olmalı")
    
    return df[[col for col in df.columns if col not in excluded_cols]]
