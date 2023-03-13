import typing

# noinspection PyPackageRequirements
from grpc import Compression, aio, ssl_channel_credentials  # type: ignore

# noinspection PyPackageRequirements
from grpc.aio import ChannelArgumentType  # type: ignore

from .auth import AuthApi
from .kv import KVApi
from .lease import LeaseApi
from .utils import AuthInterceptor

if typing.TYPE_CHECKING:
    from grpc.aio._channel import Channel  # type: ignore


_GRPC_OPTIONS = typing.Sequence[typing.Tuple[str, typing.Any]]


class Client:
    def __init__(
        self,
        endpoint: str,
        ssl: bool = False,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        ca_cert: typing.Optional[bytes] = None,
        cert_key: typing.Optional[bytes] = None,
        cert_cert: typing.Optional[bytes] = None,
        grpc_options: typing.Optional[ChannelArgumentType] = None,
        grpc_compression: typing.Optional[Compression] = None,
        timeout: typing.Optional[int] = None,
    ):
        self.endpoint = endpoint
        self.ssl = ssl
        self.interceptors = None
        if username:
            self.interceptors = [AuthInterceptor(username, password, self)]
        self.channel = self._create_grpc_channel(
            endpoint=endpoint,
            ssl=ssl,
            ca_cert=ca_cert,
            cert_key=cert_key,
            cert_cert=cert_cert,
            options=grpc_options,
            compression=grpc_compression,
        )
        self.default_timeout = timeout
        self.lease: LeaseApi = LeaseApi(self.channel)
        self.kv: KVApi = KVApi(self)
        self.auth: AuthApi = AuthApi(self)

    def _create_grpc_channel(
        self,
        endpoint: str,
        ssl: bool = False,
        ca_cert: typing.Optional[bytes] = None,
        cert_key: typing.Optional[bytes] = None,
        cert_cert: typing.Optional[bytes] = None,
        options: typing.Optional[ChannelArgumentType] = None,
        compression: typing.Optional[Compression] = None,
    ) -> Channel:
        if not ssl:
            channel = aio.insecure_channel(
                target=endpoint,
                options=options,
                compression=compression,
                interceptors=self.interceptors,
            )
        else:
            credentials = ssl_channel_credentials(ca_cert, cert_key, cert_cert)
            channel = aio.secure_channel(
                endpoint,
                credentials,
                options=options,
                compression=compression,
                interceptors=self.interceptors,
            )
        return channel
