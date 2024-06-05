"""
This module handles HTTP requests to retrieve the latest tag from release URLs.

It defines a function to make HTTP requests to the specified URL and extract
the latest version tag from the response.
"""

import requests

from .globals import REQUESTS_TIMEOUT


def get_latest_tag(releases_url: str) -> str:
    """
    Retrieve the latest version tag from the given releases URL.

    This function sends an HTTP GET request to the specified releases URL and
    extracts the latest version tag from the response URL.

    Arguments:
        releases_url (str): The URL to the releases page.

    Returns:
        str: The latest version tag extracted from the response URL.
    """
    response: requests.models.Response = requests.get(releases_url, timeout=REQUESTS_TIMEOUT)
    version: str = response.url.split('/')[-1]

    return version
