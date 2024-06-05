"""
This module is responsible for creating a configuration object based on command-line arguments.

It defines a function to process the arguments and produce a configuration namespace
that can be used throughout the application.
"""

from argparse import Namespace
from types import SimpleNamespace
from packaging import version as semver

from .constants import MAX_VERSION
from .versions import get_minimum_version


def create_configuration_from_arguments(args: Namespace) -> SimpleNamespace:
    """
    Create a configuration object from command-line arguments.

    This function processes the provided command-line arguments and generates a
    SimpleNamespace configuration object that holds the relevant settings and
    parameters for further processing.

    Arguments:
        args (Namespace): The parsed command-line arguments.

    Returns:
        SimpleNamespace: A namespace containing the configuration settings.
    """
    config: SimpleNamespace = SimpleNamespace()

    config.highest_only = args.highest_only
    config.include_pre_releases = args.include_pre_releases
    config.remove_patch_version = args.remove_patch_version
    config.min_version = get_minimum_version(args.min_version, args.language)
    config.max_version = semver.parse(args.max_version) if args.max_version.upper() != 'LATEST' else MAX_VERSION
    config.max_versions = args.max_versions
    config.language = args.language

    return config
