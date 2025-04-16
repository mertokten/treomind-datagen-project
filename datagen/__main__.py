import typer
from typing import List, Optional
from .reader import read_source_file

app = typer.Typer()

@app.command()
def generate(
    input_file: str = typer.Option(..., help="Girdi dosyasının yolu"),
    extension: str = typer.Option("csv", help="Dosya tipi: csv veya parquet"),
    sep: str = typer.Option(",", help="CSV dosya ayıraç karakteri"),
    excluded_cols: Optional[List[str]] = typer.Option(None, help="Hariç tutulacak kolonlar")
):
    excluded_cols = excluded_cols or []
    df = read_source_file(
        file_path=input_file,
        extension=extension,
        sep=sep,
        excluded_cols=excluded_cols
    )
    typer.echo(df.head())

if __name__ == "__main__":
    app()
