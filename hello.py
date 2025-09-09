import click
import glob

@click.command()
@click.option("--path", default=".", help="Path to search")
@click.option("--file-type", default="py", help="File type to search")
def search(path, file_type):
    results = glob.glob(f"{path}/*.{file_type}")
    click.secho(f"Found {len(results)} file(s)", fg="yellow")
    for r in results:
        click.secho(r, fg="blue")

if __name__ == "__main__":
    search()