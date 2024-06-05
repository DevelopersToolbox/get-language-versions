"""
This module provides functionality to list the supported programming languages.

It defines a function to print the supported languages in a nicely formatted manner.
"""
from types import SimpleNamespace
from typing import List

from .constants import SUPPORTED_LANGUAGES


def list_supported_languages() -> None:
    """
    List the supported programming languages.

    This function prints the supported programming languages as a comma-separated list
    with a header.
    """
    languages: str = ", ".join(SUPPORTED_LANGUAGES)
    print(f"Support Languages: {languages}")


def list_language_versions(config: SimpleNamespace, versions: List[str]) -> None:
    """
    List the versions that have been found for a given language.

    This function prints the versions as a comma-separated list with a header.
    """
    languages: str = ", ".join(versions)
    print(f"{config.language} Versions: {languages}")
