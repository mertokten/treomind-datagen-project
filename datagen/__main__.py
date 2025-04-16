import time
import typer
from typing import List, Optional
from typing_extensions import Annotated
from .utils import version_callback
from .reader import read_source_file
from .processor import process_data
from .writer import write_batch

from tqdm import tqdm

app = typer.Typer()

@app.command()
def generate(
    input_file: str = typer.Option(
        help="Girdi dosyasının yolu"
    ),
    extension: str = typer.Option(
        "csv", 
        help="Dosya tipi: csv veya parquet"
    ),
    sep: str = typer.Option(
        ",", 
        help="CSV dosya ayıraç karakteri"
    ),
    excluded_cols: Optional[List[str]] = typer.Option(
        [], 
        help="Hariç tutulacak kolonlar"
    ),
    batch_size: int = typer.Option(
        10,
        help="Bir batch'teki kayıt sayısı"
    ),
    shuffle: bool = typer.Option(
        False,
        help="Veri karıştırılsın mı?"
    ),
    repeat: int = typer.Option(
        1,
        help='Veri tekrar sayısı'
    ),
    batch_interval: float = typer.Option(
        0.5,
        help="Batch'ler arası bekleme süresi (sn)"
    ),
    output_folder: str = typer.Option(
        help='Çıktıların kaydedileceği klasör'
    ),
    prefix: str = typer.Option(
        'log_',
        help="Çıktı dosya adı prefix'i"
    ),
    log_sep: str = typer.Option(
        ',',
        help="Çıktı CSV'leri için ayıraç"
    ),
    output_index: bool = typer.Option(
        False,
        help="Çıktıya DataFrame index bilgisi eklensin mi?"
    ),
    is_parquet: bool = typer.Option(
        False,
        help = "Çıktı dosya tipi Parquet mi?"
    ),
    version: Annotated[
        Optional[bool],
        typer.Option(
            '--version',
            help='Get version info of the application.', 
            callback=version_callback
        )
    ] = None
):
    
    df = read_source_file(
        file_path=input_file,
        extension=extension,
        sep=sep,
        excluded_cols=excluded_cols
    )
    typer.echo("DataFrame başarılı bir şekilde getirildi. Batch'lere bölünüyor...")
    
    batches = process_data(
        df=df,
        batch_size=batch_size,
        shuffle=shuffle,
        repeat=repeat,
        batch_interval=batch_interval
    )
    
    typer.echo("DataFrame başarılı bir şekilde batch'lere bölündü.")
    
    for batch in tqdm(batches, desc="Batch'ler kaydediliyor..."):
        write_batch(
            batch=batch,
            output_folder=output_folder,
            prefix=prefix,
            log_sep=log_sep,
            output_index=output_index,
            is_parquet = is_parquet
        )
        time.sleep(batch_interval)

if __name__ == "__main__":
    app()
