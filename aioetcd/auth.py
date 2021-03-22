from __future__ import annotations
import typing
import dataclasses
from enum import IntEnum

from .common import ResponseHeader
from ._rpc_stubs import auth

from ._rpc import rpc_pb2_grpc
from ._rpc import rpc_pb2
from ._rpc import auth_pb2

if typing.TYPE_CHECKING:
    from .client import Client


class PermissionType(IntEnum):
    READ = 0
    WRITE = 1
    READWRITE = 2


@dataclasses.dataclass
class AuthenticateResponse:
    header: ResponseHeader
    token: str

    @classmethod
    def from_protobuf(
        cls, pb_value: rpc_pb2.AuthenticateResponse
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


@dataclasses.dataclass
class EnableResponse:
    header: ResponseHeader

    @classmethod
    def from_protobuf(
        cls, pb_value: rpc_pb2.AuthEnableResponse
    ) -> EnableResponse:
        return EnableResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
        )


@dataclasses.dataclass
class DisableResponse:
    header: ResponseHeader

    @classmethod
    def from_protobuf(
        cls, pb_value: rpc_pb2.AuthDisableResponse
    ) -> DisableResponse:
        return DisableResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
        )


@dataclasses.dataclass
class UserAddResponse:
    header: ResponseHeader

    @classmethod
    def from_protobuf(
        cls, pb_value: rpc_pb2.AuthUserAddResponse
    ) -> UserAddResponse:
        return UserAddResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
        )


@dataclasses.dataclass
class UserGetResponse:
    header: ResponseHeader
    roles: typing.List[str]

    @classmethod
    def from_protobuf(
        cls, pb_value: rpc_pb2.AuthUserGetResponse
    ) -> UserGetResponse:
        return UserGetResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
            roles=[role for role in pb_value.roles],
        )


class AuthApi:
    def __init__(self, client: Client):
        self._client = client
        self._auth_stub: auth.AuthStub = typing.cast(
            auth.AuthStub,
            rpc_pb2_grpc.AuthStub(channel=client.channel),  # type: ignore
        )

    async def enable(self) -> EnableResponse:
        """Enables authentication."""
        response = await self._auth_stub.AuthEnable(
            rpc_pb2.AuthEnableRequest()
        )
        return EnableResponse.from_protobuf(response)

    async def disable(self) -> DisableResponse:
        """disables authentication."""
        response = await self._auth_stub.AuthDisable(
            rpc_pb2.AuthDisableRequest()
        )
        return DisableResponse.from_protobuf(response)

    async def authenticate(
        self, name: str, password: str
    ) -> AuthenticateResponse:
        """processes an authenticate request."""
        response = await self._auth_stub.Authenticate(
            rpc_pb2.AuthenticateRequest(name=name, password=password)
        )
        return AuthenticateResponse.from_protobuf(response)

    async def user_add(self, name: str, password: str) -> UserAddResponse:
        """adds a new user. User name cannot be empty."""
        if password is None:
            options = auth_pb2.UserAddOptions(no_password=True)
        else:
            options = auth_pb2.UserAddOptions(no_password=False)
        response = await self._auth_stub.UserAdd(
            rpc_pb2.AuthUserAddRequest(
                name=name, password=password, options=options
            )
        )
        return UserAddResponse.from_protobuf(response)

    async def user_get(self, name: str) -> UserGetResponse:
        """gets detailed user information."""
        response = await self._auth_stub.UserGet(
            rpc_pb2.AuthUserGetRequest(name=name)
        )
        return UserGetResponse.from_protobuf(response)

    # async def user_list(self):
    #     ...

    # async def user_delete(self, name: str):
    #     ...

    # async def user_change_password(self, name: str, password: str):
    #     ...

    # async def user_grant_role(self, user: str, role: str):
    #     ...

    # async def user_revoke_role(self, name: str, role: str):
    #     ...

    # async def role_add(self, name: str):
    #     ...

    # async def role_get(self, role: str):
    #     ...

    # async def role_list(self):
    #     ...

    # async def role_delete(self, role: str):
    #     ...

    # async def role_grant_permission(self, name: str, permission: Permission):
    #     ...

    # async def role_revoke_permission(
    #     self, role: str, key: bytes, range_end: bytes
    # ):
    #     ...
