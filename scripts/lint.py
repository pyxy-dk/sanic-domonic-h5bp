#!/usr/bin/env python
from subprocess import run


def run_with_separator(args):
    """Print a horizontal rule to console and run a subprocess."""
    print("\n", "=" * 80, "\n")
    print(" ".join(args))
    return run(args, check=False)


def lint() -> int:
    ISORT = run_with_separator(["isort", ".", "--atomic",])
    BLACK = run_with_separator(["black", "--safe", "."])
    return ISORT.returncode + BLACK.returncode


if __name__ == "__main__":
    raise SystemExit(lint())
