import typer
from typing import List, Optional
from .reader import read_source_file
from .processor import process_data

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
    )
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

if __name__ == "__main__":
    app()
