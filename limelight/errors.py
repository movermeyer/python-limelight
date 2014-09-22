# -*- coding: utf-8 -*-


class LimeLightException(Exception):
    def __init__(self, *args, **kwargs):
        """
        :param response: A reference to the request object that raised the exception
        :type response: limelight.request.Request
        """
        response = kwargs.pop('response', None)
        if response is not None:
            self.response = response
        super(LimeLightException, self).__init__(*args, **kwargs)


class ImproperlyConfigured(LimeLightException):
    pass


# noinspection PyShadowingBuiltins
class ConnectionError(LimeLightException):
    pass


class NoPreviousOrder(LimeLightException):
    pass


class TransactionDeclined(LimeLightException):
    pass


class CouldNotFindProspectRecord(LimeLightException):
    pass


class ValidationError(LimeLightException):
    pass