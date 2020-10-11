import asyncio
import weakref

from typing import Callable, Union

from grpc.aio import (  # type: ignore
    StreamStreamClientInterceptor,
    UnaryUnaryClientInterceptor,
    ClientCallDetails,
)
from grpc.aio._call import UnaryUnaryCall, UnaryStreamCall, StreamStreamCall  # type: ignore
from grpc.aio._typing import (  # type: ignore
    RequestType,
    ResponseType,
    RequestIterableType,
    ResponseIterableType,
)
from grpc import AuthMetadataPlugin, metadata_call_credentials  # type: ignore


# class _EtcdTokenCallCredentials(AuthMetadataPlugin):
#     def __init__(self, access_token):
#         self._access_token = access_token
#
#     def __call__(self, context, callback):
#         metadata = (("token", self._access_token),)
#         callback(metadata, None)

AUTHENTICATED_METHOD = b"/etcdserverpb.Auth/Authenticate"


class AuthInterceptor(
    StreamStreamClientInterceptor, UnaryUnaryClientInterceptor
):
    def __init__(self, username, password, client):
        self.username = username
        self.password = password
        self.client = weakref.ref(client)
        self._call_credentials = None
        self._metadata = None
        self._auth_lock = asyncio.Lock()

    async def _authenticate(self):
        async with self._auth_lock:
            if self._metadata is not None:  # Avoiding double authentication
                return
            response = await self.client().auth.authenticate(
                name=self.username, password=self.password
            )
            self._metadata = (("token", response.token),)

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
        _client_call_details = ClientCallDetails(
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
