"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
from argparse import Namespace
from types import SimpleNamespace
from packaging import version as semver

from .constants import MAX_VERSION
from .versions import get_minimum_version


def create_configuration_from_arguments(args: Namespace) -> SimpleNamespace:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        args (argparse.Namespace) -- _description_
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
