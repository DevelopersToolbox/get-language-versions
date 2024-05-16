#!/usr/bin/env python

"""
This script is designed to allow you to manage the labels on your GitHub repositories.

Keeping all your labels consistent makes it easier to work across multiple repositories (and organisations)
"""

from .cli import run
from .exceptions import InvalidParameters
from .notify import error, system


def main() -> None:
    """
    Execute the main routine of the script.

    This function serves as the entry point of the script. It is responsible
    for invoking the `process_arguments` function, which handles the processing
    of command-line arguments. The `main` function does not take any parameters
    and does not return any value. It ensures that the script's functionality
    is triggered correctly when the script is executed.
    """
    run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        system("\n[*] Exiting Program\n")
    except InvalidParameters as e:
        error(str(e))
