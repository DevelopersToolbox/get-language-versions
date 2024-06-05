"""
This module defines global constants and retrieves the version information for the application.

It sets up global constants used for the argument parser configuration and retrieves the version
information of the application package using the importlib.metadata module. If the package is not found,
the version is set to 'unknown'.
"""

import importlib.metadata

try:
    version: str = importlib.metadata.version('wolfsoftware.get-language-versions')
except importlib.metadata.PackageNotFoundError:
    version = 'unknown'

# Program name for the argument parser
ARG_PARSER_PROG_NAME: str = "get-language-versions"

# Description for the argument parser
ARG_PARSER_DESCRIPTION: str = "A description goes here"

# Epilog for the argument parser
ARG_PARSER_EPILOG: str = "The Epilog goes here"

# Version string to display the current version of the program
VERSION_STRING: str = f"Current version of {ARG_PARSER_PROG_NAME} is v{version}"

# Timeout duration for requests made by the program
REQUESTS_TIMEOUT: int = 5
