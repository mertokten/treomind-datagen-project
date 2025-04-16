import os
import uuid

import pandas as pd


def write_batch(
    batch: pd.DataFrame,
    output_folder: str,
    prefix: str,
    log_sep: str,
    output_index: bool,
    is_parquet: bool
):
    os.makedirs(output_folder, exist_ok=True)
    file_id = uuid.uuid4().hex[:8]
    if is_parquet: 
        file_path = os.path.join(output_folder, f"{prefix}{file_id}.parquet")
        batch.to_parquet(
            file_path,
            index=output_index,
            encoding='utf-8'
        )
    else:
        file_path = os.path.join(output_folder, f"{prefix}{file_id}.csv")
        batch.to_csv(
            file_path,
            sep=log_sep,
            index=output_index,
            encoding='utf-8'
        )
    return file_path