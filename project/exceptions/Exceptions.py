class Error(Exception):
    """Base class for other exceptions"""
    pass


class FileException(Error):
    """Error while operating with the file"""
    pass


class SheepViabilityException(Error):
    """All sheep are dead"""
    pass
