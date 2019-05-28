class AioEtcdError(Exception):
    pass


class HttpError(AioEtcdError):
    pass


class ParseError(AioEtcdError):
    pass


class EtcdError(AioEtcdError):
    def __init__(self, *args, **kwargs):
        self.error_respnse = kwargs.pop('error_response')
        super(EtcdError, self).__init__(*args, **kwargs)
