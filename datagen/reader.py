import pandas as pd

def read_source_file(file_path: str, sep: str = ",") -> pd.DataFrame:
    return pd.read_csv(file_path, sep=sep)
