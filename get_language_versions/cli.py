"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

import argparse
import sys

from types import SimpleNamespace

from .config import create_configuration_from_arguments
from .constants import SUPPORTED_LANGUAGES
from .globals import ARG_PARSER_PROG_NAME, ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, VERSION_STRING
from .process import process_languages
from .utils import list_supported_languages


# Custom type function to ensure positive integer
def positive_int(value: str) -> int:
    """
    _summary_.

    _extended_summary_

    Arguments:
        value (int): _description_

    Returns:
        _type_: _description_

    Raises:
        argparse.ArgumentTypeError: _description_
    """
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Configure the argument parser.

    Returns:
        argparse.ArgumentParser: The arguments parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION,
                                     epilog=ARG_PARSER_EPILOG)

    flags: argparse._ArgumentGroup = parser.add_argument_group('flags')
    optional_flags: argparse._ArgumentGroup = parser.add_argument_group('optional flags')
    optional: argparse._ArgumentGroup = parser.add_argument_group('optional')
    required: argparse._ArgumentGroup = parser.add_argument_group('required')

    # Command line flags
    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="show this help message and exit.")
    flags.add_argument('-v', '--version', action='version', version=VERSION_STRING, help="Show program's version number and exit.")

    optional_flags.add_argument('-H', '--highest-only', action='store_true', help='Only return the highest version found.')
    optional_flags.add_argument('-L', '--list-languages', action='store_true', help='List the supported languages')
    optional_flags.add_argument('-P', '--include-pre-releases', action='store_true', help='Include pre-release versions')
    optional_flags.add_argument('-R', '--remove-patch-version', action='store_true', help='Strip the patch version from the returned versions.')

    # Optional arguments
    optional.add_argument('-m', '--min-version', type=str, default='EOL', help='The minimum version to start from')
    optional.add_argument('-M', '--max-version', type=str, default='LATEST', help='The maximum version to include')
    optional.add_argument('-V', '--max-versions', type=positive_int, default=0, help='The maximum number of versions to return')

    # Required arguments
    required.add_argument('-l', '--language', type=str, choices=SUPPORTED_LANGUAGES, help='The language to check.')

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process the command line arguments.

    Setup the arguments parser, parser the arguments, validate the input and then action the requested changed.
    """
    args: argparse.Namespace = parser.parse_args()

    if args.list_languages and args.language:
        raise argparse.ArgumentTypeError("argument -l/--language: not allowed with argument -L/--list-languages")

    if args.list_languages:
        list_supported_languages()
        sys.exit(0)

    if not args.language:
        raise argparse.ArgumentTypeError("the following arguments are required: -l/--language")

    args.language = args.language.lower()

    if args.language not in SUPPORTED_LANGUAGES:
        raise argparse.ArgumentTypeError("Unsupported language [use -L/--list-languages to see a list of supported languages]")

    if args.remove_patch_version and args.include_pre_releases:
        raise argparse.ArgumentTypeError("argument -P/--include-pre-released: not allowed with argument -R/--remove-patch-version")

    return args


def run() -> None:
    """
    _summary_.

    _extended_summary_
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
    else:
        config: SimpleNamespace = create_configuration_from_arguments(args)
        versions: list = process_languages(config)

    # We need some form of output handling
    print(versions)
