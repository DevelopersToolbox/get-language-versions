#!/usr/bin/env python

"""
This script is designed to allow you to manage the labels on your GitHub repositories.

Keeping all your labels consistent makes it easier to work across multiple repositories (and organisations)
"""
import sys

from signal import signal, SIGTERM
from typing import NoReturn

from .cli import run
from .notify import system


def sigterm_handler(_, __) -> NoReturn:
    """
    _summary_.

    _extended_summary_

    Arguments:
        _ (_type_): _description_
        __ (_type_): _description_

    Returns:
        NoReturn: _description_

    Raises:
        SystemExit: _description_
    """
    raise SystemExit(1)


def main() -> None:
    """
    Execute the main routine of the script.

    This function serves as the entry point of the script. It is responsible
    for invoking the `process_arguments` function, which handles the processing
    of command-line arguments. The `main` function does not take any parameters
    and does not return any value. It ensures that the script's functionality
    is triggered correctly when the script is executed.
    """
    signal(SIGTERM, sigterm_handler)

    try:
        run()
    except KeyboardInterrupt:
        system("\n[*] Exiting Program\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
