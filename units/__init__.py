class UnitsManager(object):
    """
    Class responsible to manage the unit converters
    of this application.
    """
    _units = [
    ]

    def __iter__(self):
        return (x for x in self._units)
