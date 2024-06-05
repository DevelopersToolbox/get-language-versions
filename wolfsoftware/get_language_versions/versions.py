"""
This module handles the retrieval and processing of version information for various programming languages.

It defines functions to fetch the minimum and stable versions, as well as to parse and handle version
data from different sources and formats.
"""

import datetime
import requests
from bs4 import BeautifulSoup
from packaging import version as semver
from .constants import MAX_VERSION, MIN_VERSION, URLS
from .globals import REQUESTS_TIMEOUT
from .tags import get_latest_tag


def get_minimum_version_from_oel(language: str) -> semver.Version:
    """
    Get the minimum version from the EOL (End Of Life) URL.

    The default value for min-version is "EOL" so we need to have a way to get the min-version from the
    EOL URL.

    Arguments:
        language (str): The supported language to use to locate the correct EOL URL.

    Returns:
        semver.Version: The minimum "supported" version.
    """
    versions_url: str = URLS[language]["eol_url"]
    min_version: semver.Version = MAX_VERSION

    for release in requests.get(versions_url, timeout=REQUESTS_TIMEOUT).json():
        try:
            semver.Version(release['cycle'])
        except semver.InvalidVersion:
            continue

        if release['eol'] is True:
            continue

        if release['eol'] is False:
            min_version = min(min_version, semver.parse(release['cycle']))
            continue

        if datetime.date.today() < datetime.date.fromisoformat(release['eol']):
            min_version = semver.parse(release['cycle'])

    return min_version


def get_minimum_version(min_version_str: str, language: str) -> semver.Version:
    """
    Get the minimum version based on the input string and language.

    There are multiple ways to define the min-version we want to use, this is a simple wrapper to correctly set the right version.

    Arguments:
        min_version_str (str): The min-version as supplied to the action by the user (or the default if none is supplied).
        language (str): The supported language.

    Returns:
        semver.Version: The minimum version for the supplied language.
    """
    min_version: semver.Version

    if min_version_str.upper() == 'EOL':
        min_version = get_minimum_version_from_oel(language)
    elif min_version_str.upper() == 'ALL':
        min_version = MIN_VERSION
    else:
        min_version = semver.parse(min_version_str)
    return min_version


def get_perl_versions(stable_versions: dict) -> list:
    """
    Get Perl versions from the returned dataset.

    Different version URLs return the version data in different formats, this handles the data for Perl only.

    Arguments:
        stable_versions (dict): The dataset returned from the versions URL.

    Returns:
        list: A list containing just the version numbers.
    """
    versions: list = []

    for version in stable_versions:
        try:
            if semver.Version(version):
                versions.append(version)
        except semver.InvalidVersion:
            continue

    return versions


def get_php_versions(stable_versions: dict) -> list:
    """
    Get PHP versions from the returned dataset.

    Different version URLs return the version data in different formats, this handles the data for PHP only.

    Arguments:
        stable_versions (dict): The dataset returned from the versions URL.

    Returns:
        list: A list containing just the version numbers.
    """
    versions: list = []

    for version_object in stable_versions:
        version: str = f"{version_object['major']}.{version_object['minor']}.{version_object['release']}"

        try:
            if semver.Version(version):
                versions.append(version)
        except semver.InvalidVersion:
            continue

    return versions


def get_ruby_versions(stable_versions: dict) -> list:
    """
    Get Ruby versions from the returned dataset.

    Different version URLs return the version data in different formats, this handles the data for Ruby only.

    Arguments:
        stable_versions (dict): The dataset returned from the versions URL.

    Returns:
        list: A list containing just the version numbers.
    """
    versions: list = []

    for version in stable_versions["ruby"]:
        try:
            if semver.Version(version):
                versions.append(version)
        except semver.InvalidVersion:
            continue

    return versions


def get_terraform_versions(stable_versions: dict) -> list:
    """
    Get Terraform versions from the returned dataset.

    Different version URLs return the version data in different formats, this handles the data for Terraform only.

    Arguments:
        stable_versions (dict): The dataset returned from the versions URL.

    Returns:
        list: A list containing just the version numbers.
    """
    versions: list = []

    soup: BeautifulSoup = BeautifulSoup(stable_versions, features="html.parser")
    for link in soup.findAll('a'):
        version: str = link['href'].replace('/terraform/', '').replace('/', '')
        try:
            semver.Version(version)
        except semver.InvalidVersion:
            continue
        else:
            versions.append(version)

    return versions


def get_versions(stable_versions: dict) -> list:
    """
    Get versions from the returned dataset.

    Different version URLs return the version data in different formats, this handles the data for Go, Node.js, and Python.

    Arguments:
        stable_versions (dict): The dataset returned from the versions URL.

    Returns:
        list: A list containing just the version numbers.
    """
    versions: list = []

    for version_object in stable_versions:
        version: str = version_object['version']

        try:
            if semver.Version(version):
                versions.append(version)
        except semver.InvalidVersion:
            continue

    return versions


def get_stable_versions(language: str, return_json: bool = True) -> dict:
    """
    Get a list of stable versions for a given language.

    For a given language, locate the current stable (supported) versions.

    Arguments:
        language (str): The supported language to use.

    Returns:
        dict: The list of stable (supported) versions available.
    """
    versions_url: str = URLS[language]["versions_url"]

    if "releases_url" in URLS[language]:
        latest_tag: str = get_latest_tag(URLS[language]["releases_url"])
        versions_url = versions_url.replace('LATEST_TAG', latest_tag)

    if return_json is True:
        return requests.get(versions_url, timeout=REQUESTS_TIMEOUT).json()
    return requests.get(versions_url, timeout=REQUESTS_TIMEOUT).text
