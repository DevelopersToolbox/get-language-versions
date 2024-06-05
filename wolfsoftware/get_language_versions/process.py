"""
This module processes versions of various programming languages and tools.

It defines functions to compare versions against minimum and maximum boundaries, process lists
of versions to ensure they meet specified criteria, and handle different languages using the
provided configuration.
"""

from types import SimpleNamespace
from packaging import version as semver
from yaspin import yaspin

from .versions import get_versions, get_perl_versions, get_php_versions, get_ruby_versions, get_stable_versions, get_terraform_versions


def compare_min_max_value(versions_dict: dict, version: str, min_version: semver.Version, max_version: semver.Version) -> dict:
    """
    Compare the given version against minimum and maximum boundaries.

    This function checks if the given version is within the specified minimum
    and maximum version range. If it is, the version is added to the versions
    dictionary if it's not already present or if it's a higher version than
    the existing one.

    Arguments:
        versions_dict (dict): The dictionary of valid versions.
        version (str): The current version to compare.
        min_version (semver.Version): The minimum defined version.
        max_version (semver.Version): The maximum defined version.

    Returns:
        dict: The updated versions dictionary.
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
    Process the list of stable versions to ensure they meet criteria.

    This function filters and processes the list of stable versions to ensure they are
    within the specified minimum and maximum version boundaries. It also handles pre-release
    versions and patch version removal based on the provided flags.

    Arguments:
        stable_versions (list): The list of stable versions.
        min_version (semver.Version): The minimum identified version.
        max_version (semver.Version): The maximum identified version.
        include_pre (bool): Flag to include pre-releases.
        remove_patch (bool): Flag to remove patch versions.

    Returns:
        list: The complete list of versions within the defined bounds.
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
    Process versions for the specified language based on the configuration.

    This function retrieves stable versions for the specified language and processes
    them according to the configuration settings, including minimum and maximum versions,
    inclusion of pre-releases, and removal of patch versions. It also handles different
    languages using specific processing functions.

    Arguments:
        config (SimpleNamespace): The configuration settings.

    Returns:
        list: The list of processed versions.
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
