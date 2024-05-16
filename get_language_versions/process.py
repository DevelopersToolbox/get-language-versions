"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from types import SimpleNamespace

from packaging import version as semver
from yaspin import yaspin

from .versions import get_versions, get_perl_versions, get_php_versions, get_ruby_versions, get_stable_versions, get_terraform_versions


def compare_min_max_value(versions_dict: dict, version: str, min_version: semver.Version, max_version: semver.Version) -> dict:
    """
    Compare version against min and max.

    Compare the current version against the min and max to see if it within the range we want.

    Arguments:
        versions_dict (dict) -- The dictionary of valid versions.
        version (str) -- The current version we are comparing.
        min_version (str) -- The minimum defined version.
        max_version (str) -- The maximum defined version.

    Returns:
        dict -- The updated versions dictionary.
    """
    major_minor: semver.Version = semver.parse('.'.join(version.split('.')[:2]))

    if min_version <= major_minor <= max_version:
        if major_minor in versions_dict:
            if semver.parse(versions_dict[major_minor]) < semver.parse(version):
                versions_dict[major_minor] = version
        else:
            versions_dict[major_minor] = version

    return versions_dict


def process_versions(stable_versions: list, min_version: semver.Version, max_version: semver.Version, include_pre: bool, remove_patch: bool) -> list:
    """
    Process the list of versions.

    Process the list of versions, and ensure they are within the min-version and max-version.

    Arguments:
        stable_versions (list) -- The list of stable versions.
        min_version (str) -- The minimum identified version.
        max_version (str) -- The maximum identified version.
        parsed_include_prereleases (bool) -- Should we include pre-releases?

    Returns:
        list -- The complete list of versions within our defined bounds.
    """
    versions_dict: dict = {}

    for version in stable_versions:
        try:
            semver.Version(version)
        except semver.InvalidVersion:
            continue

        if not include_pre and semver.parse(version).is_prerelease:
            continue

        if remove_patch:
            version_str: str = '.'.join(version.split('.')[:2])
        else:
            version_str = version

        versions_dict = compare_min_max_value(versions_dict, version_str, min_version, max_version)

    versions: list = list(versions_dict.values())
    versions = sorted(versions, key=lambda x: [int(i) if i.isdigit() else i for i in x.split('.')])
    return versions


def process_languages(config: SimpleNamespace) -> list:
    """
    _summary_.

    _extended_summary_

    Arguments:
        args (argparse.Namespace): _description_
    """
    stable_versions: dict = {}
    versions: list = []

    with yaspin(text=f"Getting stable versions for {config.language}", color="cyan") as spinner:

        if config.language == "terraform":
            stable_versions = get_stable_versions(config.language, False)
        else:
            stable_versions = get_stable_versions(config.language)

        if config.language == "perl":
            versions = get_perl_versions(stable_versions)
        elif config.language == "php":
            versions = get_php_versions(stable_versions)
        elif config.language == "ruby":
            versions = get_ruby_versions(stable_versions)
        elif config.language == "terraform":
            versions = get_terraform_versions(stable_versions)
        else:
            versions = get_versions(stable_versions)

        versions = process_versions(versions, config.min_version, config.max_version, config.include_pre_releases, config.remove_patch_version)

        if config.highest_only:
            versions = versions[-1]
        else:
            if config.max_versions and config.max_versions > 0:
                versions = versions[-config.max_versions:]

    spinner.ok('Done')

    return versions
