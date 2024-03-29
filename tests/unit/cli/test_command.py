import click
from click.testing import CliRunner
from cli.simplewiki_cli import hello


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(hello, ["Peter"])
    assert result.exit_code == 0
    assert result.output == "Hello Peter!\n"

