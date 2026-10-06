"""Tests for the command-line interface."""

import pytest

from gpt import __version__
from gpt.cli import main


def test_cli_without_arguments_prints_help(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0

    output = capsys.readouterr().out
    assert "usage: gpt" in output
    assert "nomosmath GPT tools" in output


def test_cli_reports_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit, match="0"):
        main(["--version"])

    assert capsys.readouterr().out.strip() == f"gpt {__version__}"
