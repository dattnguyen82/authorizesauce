class AuthorizeError(Exception):
    """Base class for all Authorize.net client errors."""

class AuthorizeConnectionError(AuthorizeError):
    """Error communicating with the Authorize.net API."""

class AuthorizeResponseError(AuthorizeError):
    """Error response code returned from API."""

class AuthorizeInvalidError(AuthorizeError):
    """Invalid information provided."""
