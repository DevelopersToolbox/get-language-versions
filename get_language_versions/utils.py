"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from .constants import SUPPORTED_LANGUAGES


def list_supported_languages() -> None:
    """
    _summary_.

    _extended_summary_
    """
    for lang in SUPPORTED_LANGUAGES:
        print(lang)
