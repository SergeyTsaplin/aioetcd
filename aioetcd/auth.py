from __future__ import annotations
import typing
import dataclasses
from enum import Enum

from .common import ResponseHeader
from ._rpc_stubs import auth

from ._rpc import rpc_pb2_grpc
from ._rpc import rpc_pb2

if typing.TYPE_CHECKING:
    from .client import Client


class PermissionType(Enum):
    READ = 0
    WRITE = 1
    READWRITE = 2


@dataclasses.dataclass
class AuthenticateResponse:
    header: ResponseHeader
    token: str

    @classmethod
    def from_protobuf(
        cls, pb_value: auth.AuthenticateResponseProto
    ) -> AuthenticateResponse:
        return AuthenticateResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
            token=pb_value.token,
        )


@dataclasses.dataclass
class UserAddOptions:
    no_password: bool = False


@dataclasses.dataclass
class Permission:
    permission_type: PermissionType
    key: bytes
    range_end: bytes


class AuthApi:
    def __init__(self, client: Client):
        self._client = client
        self._auth_stub = rpc_pb2_grpc.AuthStub(channel=client.channel)

    async def enable(self):
        ...

    async def disable(self):
        ...

    async def authenticate(self, name, password) -> AuthenticateResponse:
        response = await self._auth_stub.Authenticate(
            rpc_pb2.AuthenticateRequest(name=name, password=password)
        )
        return AuthenticateResponse.from_protobuf(response)

    async def user_add(self, name: str, password: str, options):
        ...

    async def user_get(self, name: str):
        ...

    async def user_list(self):
        ...

    async def user_delete(self, name: str):
        ...

    async def user_change_password(self, name: str, password: str):
        ...

    async def user_grant_role(self, user: str, role: str):
        ...

    async def user_revoke_role(self, name: str, role: str):
        ...

    async def role_add(self, name: str):
        ...

    async def role_get(self, role: str):
        ...

    async def role_list(self):
        ...

    async def role_delete(self, role: str):
        ...

    async def role_grant_permission(self, name: str, permission: Permission):
        ...

    async def role_revoke_permission(
        self, role: str, key: bytes, range_end: bytes
    ):
        ...
