from __future__ import annotations
import asyncio
import weakref
import typing

from typing import Callable, Union, Optional

from grpc.aio import (  # type: ignore
    StreamStreamClientInterceptor,
    UnaryUnaryClientInterceptor,
    ClientCallDetails,
)
from grpc.aio._call import (  # type: ignore
    UnaryUnaryCall,
    UnaryStreamCall,
    StreamStreamCall,
)
from grpc.aio._typing import (  # type: ignore
    RequestType,
    ResponseType,
    RequestIterableType,
    ResponseIterableType,
)


if typing.TYPE_CHECKING:
    from .client import Client


AUTHENTICATED_METHOD = b"/etcdserverpb.Auth/Authenticate"


class AuthInterceptor(
    StreamStreamClientInterceptor, UnaryUnaryClientInterceptor  # type: ignore
):
    def __init__(
        self, username: Optional[str], password: Optional[str], client: Client
    ):
        self.username = username
        self.password = password
        self.client = weakref.ref(client)
        self._call_credentials = None
        self._metadata: typing.Optional[
            typing.Tuple[typing.Tuple[str, str]]
        ] = None
        self._auth_lock = asyncio.Lock()

    async def _authenticate(self) -> None:
        async with self._auth_lock:
            if self._metadata is not None:  # Avoiding double authentication
                return
            client = self.client()
            if client is None:
                raise RuntimeError("client does not exist")
            if self.username is not None and self.password is not None:
                response = await client.auth.authenticate(
                    name=self.username, password=self.password
                )
                self._metadata = (("token", response.token),)
            else:
                raise RuntimeError("missing username or password")

    async def intercept_stream_stream(
        self,
        continuation: Callable[
            [ClientCallDetails, RequestType], UnaryStreamCall
        ],
        client_call_details: ClientCallDetails,
        request_iterator: RequestIterableType,
    ) -> Union[ResponseIterableType, StreamStreamCall]:
        if self.username and self._metadata is None:
            await self._authenticate()
        client_call_details = ClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            metadata=self._metadata,
            credentials=client_call_details.credentials,
            wait_for_ready=client_call_details.wait_for_ready,
        )
        return await continuation(client_call_details, request_iterator)

    async def intercept_unary_unary(
        self,
        continuation: Callable[
            [ClientCallDetails, RequestType], UnaryUnaryCall
        ],
        client_call_details: ClientCallDetails,
        request: RequestType,
    ) -> Union[UnaryUnaryCall, ResponseType]:
        if AUTHENTICATED_METHOD == client_call_details.method:
            return await continuation(client_call_details, request)
        if self.username and self._metadata is None:
            await self._authenticate()
        _client_call_details = ClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            metadata=self._metadata,
            credentials=client_call_details.credentials,
            wait_for_ready=client_call_details.wait_for_ready,
        )
        return await continuation(_client_call_details, request)
