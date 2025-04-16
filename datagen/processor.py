import time
from datetime import datetime

import pandas as pd
from tqdm import tqdm


def process_data(
    df: pd.DataFrame,
    batch_size: int,
    shuffle: bool,
    repeat: int,
    batch_interval: float
):
    
    repeat_iter = range(repeat)
    df_iter = range(0, len(df), batch_size)
    
    if shuffle:
        df = (
            df
            .sample(frac=1)
            .reset_index(drop=True)
        )
    
    batches = []
    for _ in tqdm(repeat_iter, desc="Veri seti tekrar ediliyor..."):
        for start in tqdm(df_iter, desc="Batch oluşturuluyor..."):
            batch = (
                df
                .iloc[start:start+batch_size]
                .copy()
            )
            batch['event_time'] = datetime.now().isoformat()
            batches.append(batch)
            time.sleep(batch_interval)
    return batches
