import typing
import asyncio
import aiogrpc
from grpc import aio, ssl_channel_credentials, Compression
from grpc.aio import ChannelArgumentType

from .lease import LeaseApi
from .utils import AuthInterceptor


if typing.TYPE_CHECKING:
    from concurrent.futures._base import Executor


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
        timeout: int = 5,
    ):
        self.endpoint = endpoint
        self.ssl = ssl
        self.interceptors = None
        if username:
            self.interceptors = [AuthInterceptor(username, password, self)]
        self._channel = self._create_grpc_channel(
            endpoint=endpoint,
            ssl=ssl,
            ca_cert=ca_cert,
            cert_key=cert_key,
            cert_cert=cert_cert,
            options=grpc_options,
            compression=grpc_compression,
        )
        self.lease: LeaseApi = LeaseApi(self._channel)

    def _create_grpc_channel(
        self,
        endpoint: str,
        ssl: bool = False,
        ca_cert: bytes = None,
        cert_key: bytes = None,
        cert_cert: bytes = None,
        options: typing.Optional[ChannelArgumentType] = None,
        compression: typing.Optional[Compression] = None,
    ):
        if not ssl:
            channel = aio.insecure_channel(
                target=endpoint,
                options=options,
                compression=compression,
                interceptors=self.interceptors,
            )
        else:
            credentials = ssl_channel_credentials(
                ca_cert, cert_key, cert_cert
            )
            channel = aio.secure_channel(
                endpoint,
                credentials,
                options=options,
                compression=compression,
                interceptors=self.interceptors,
            )
        return channel
