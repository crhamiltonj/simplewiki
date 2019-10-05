import click


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    click.echo("Dropped the database...")


@click.command()
@click.argument("name")
def hello(name):
    click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()

