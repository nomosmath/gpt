"""Command-line interface for the project."""

import argparse
from collections.abc import Sequence

from gpt import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="gpt",
        description="A foundation for nomosmath GPT tools.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface."""
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0
