import os

import typer

__version__ = '0.1.0'

PACKAGE_PATH = os.path.dirname(
    os.path.abspath(f'{__file__}')
)

DATA_DIR = os.path.abspath(
    os.path.join(f'{PACKAGE_PATH}', '..', 'data')
)

def version_callback(
    value: bool
):
    if value:
        typer.echo(f"Treomind Datagen Version: {__version__}")
        raise typer.Exit()
