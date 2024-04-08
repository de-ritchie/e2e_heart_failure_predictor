"""This module holds the model classes of custom exception"""

class DatabaseException(Exception):

    """
    Custom Exception class, exception raised when error occurrs in connecting with MongoDB

    Parameters:
    message: Error message detail
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)

class FeatureStoreException(Exception):

    """
    Custom Exception class, exception raised when error occurrs in Feature Store module

    Parameters:
    message: Error message detail
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
