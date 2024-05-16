"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from importlib.metadata import version

# This is a dirty hack to the get the package name
DIST_NAME: str = __name__.split('.', maxsplit=1)[0]

ARG_PARSER_PROG_NAME: str = "get-language-versions"
ARG_PARSER_DESCRIPTION: str = "A description goes here"
ARG_PARSER_EPILOG: str = "The Epilog goes here"

VERSION_STRING: str = "Current version of " + ARG_PARSER_PROG_NAME + " is v" + version(DIST_NAME)

# Make this a command line option!
REQUESTS_TIMEOUT: int = 5
