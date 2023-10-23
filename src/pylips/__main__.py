import click
import os


@click.group()
def cli():
    return 0


if __name__ == "__main__":
    SystemExit(cli())
