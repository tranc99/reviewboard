from __future__ import unicode_literals


class OwnershipError(ValueError):
    pass


class PermissionError(Exception):
    def __init__(self):
        Exception.__init__(self, None)
