from typing import Callable, Union
import asyncio
import weakref

from grpc.aio import StreamStreamClientInterceptor, UnaryUnaryClientInterceptor, ClientCallDetails
from grpc.aio._call import UnaryUnaryCall, UnaryStreamCall, StreamStreamCall
from grpc.aio._typing import RequestType, ResponseType, RequestIterableType, ResponseIterableType
from grpc import AuthMetadataPlugin, metadata_call_credentials


class _EtcdTokenCallCredentials(AuthMetadataPlugin):

    def __init__(self, access_token):
        self._access_token = access_token

    def __call__(self, context, callback):
        metadata = (("token", self._access_token),)
        callback(metadata, None)


class AuthInterceptor(StreamStreamClientInterceptor, UnaryUnaryClientInterceptor):
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
            token = await self.client().authenticate(username=self.username, password=self.password)
            self._metadata = (("token", token),)
            self._call_credentials = metadata_call_credentials(_EtcdTokenCallCredentials(token))

    async def intercept_stream_stream(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryStreamCall],
        client_call_details: ClientCallDetails,
        request_iterator: RequestIterableType
    ) -> Union[ResponseIterableType, StreamStreamCall]:
        if self.username and self._metadata is None:
            await self._authenticate()
        client_call_details.credentials = self._call_credentials
        client_call_details.metadata = self._metadata
        return await continuation(client_call_details, request_iterator)

    async def intercept_unary_unary(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryUnaryCall],
        client_call_details: ClientCallDetails,
        request: RequestType
    ) -> Union[UnaryUnaryCall, ResponseType]:
        if "/etcdserverpb.Auth/Authenticate" == client_call_details.method:
            return await continuation(client_call_details, request)
        if self.username and self._metadata is None:
            await self._authenticate()
        client_call_details.credentials = self._call_credentials
        client_call_details.metadata = self._metadata
        return await continuation(client_call_details, request)


