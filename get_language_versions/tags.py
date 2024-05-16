"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

import requests

from .globals import REQUESTS_TIMEOUT


def get_latest_tag(releases_url: str) -> str:
    """
    Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        releases_url (str) -- _description_

    Returns:
        str -- _description_
    """
    response: requests.models.Response = requests.get(releases_url, timeout=REQUESTS_TIMEOUT)
    version: str = response.url.split('/')[-1]

    return version
