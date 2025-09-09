"""Simple CLI tool to search files by extension using Click."""

import glob
import click

@click.command()
@click.option("--path", default=".", help="Path to search")
@click.option("--file-type", default="py", help="File type to search")
def search(path, file_type):
    """Search for files with given extension under the specified path."""
    results = glob.glob(f"{path}/*.{file_type}")
    click.secho(f"Found {len(results)} file(s)", fg="yellow")
    for r in results:
        click.secho(r, fg="blue")

if __name__ == "__main__":
    search()  # pylint: disable=no-value-for-parameter

    