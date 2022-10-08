class Error(Exception):
    """Base class for other exceptions"""
    pass


class file_exception(Error):
    """Error while operating with the file"""
    pass


class sheep_viability_exception(Error):
    """All sheep are dead"""
    pass


class logic_exception(Error):
    """Error in simulation logic"""
    pass
