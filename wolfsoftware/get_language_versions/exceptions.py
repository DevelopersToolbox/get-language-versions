"""
This module defines custom exceptions used throughout the application.

It includes a base custom exception class that can be extended for specific error
handling needs.
"""


class CustomException(Exception):
    """
    A base class for custom exceptions in the application.

    This class can be extended to create specific exceptions with additional
    context or information as needed.

    Arguments:
        Exception (Exception): Inherits from the base Exception class.
    """
