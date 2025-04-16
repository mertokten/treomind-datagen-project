import typer

app = typer.Typer()

@app.command()
def generate():
    typer.echo("Generate function is set up (logic will be added in future steps)")

if __name__ == "__main__":
    app()
