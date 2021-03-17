from __future__ import annotations
import typing
from typing_extensions import Protocol
from enum import IntEnum

from grpc.aio._channel import Channel  # type: ignore

from .common import ResponseHeader


class UserAddOptions(Protocol):
    no_password: bool

    def __init__(self, no_password: bool):
        ...


class PermissionType(IntEnum):
    READ = 0
    WRITE = 1
    READWRITE = 2


class Permission(Protocol):
    permType: PermissionType
    key: bytes
    range_end: bytes


class AuthEnableRequest(Protocol):
    def __init__(self) -> None:
        ...


class AuthEnableResponse(Protocol):
    header: ResponseHeader


class AuthDisableRequest(Protocol):
    def __init__(self) -> None:
        ...


class AuthDisableResponse(Protocol):
    header: ResponseHeader


class AuthenticateRequest(Protocol):
    def __init__(self, name: str, password: str):
        ...


class AuthenticateResponse(Protocol):
    header: ResponseHeader
    token: str


class AuthUserAddRequest(Protocol):
    def __init__(
        self,
        name: str,
        password: typing.Optional[str],
        options: UserAddOptions,
    ):
        ...


class AuthUserAddResponse(Protocol):
    header: ResponseHeader


class AuthUserGetRequest(Protocol):
    def __init__(self, name: str):
        ...


class AuthUserGetResponse(Protocol):
    header: ResponseHeader
    roles: typing.List[str]


class AuthUserListRequest(Protocol):
    def __init__(self) -> None:
        ...


class AuthUserListResponse(Protocol):
    header: ResponseHeader
    users: typing.List[str]


class AuthUserDeleteRequest(Protocol):
    def __init__(self, name: str):
        ...


class AuthUserDeleteResponse(Protocol):
    header: ResponseHeader


class AuthUserChangePasswordRequest(Protocol):
    def __init__(self, name: str, password: str):
        ...


class AuthUserChangePasswordResponse(Protocol):
    header: ResponseHeader


class AuthUserGrantRoleRequest(Protocol):
    def __init__(self, user: str, role: str):
        ...


class AuthUserGrantRoleResponse(Protocol):
    header: ResponseHeader


class AuthUserRevokeRoleRequest(Protocol):
    def __init__(self, user: str, role: str):
        ...


class AuthUserRevokeRoleResponse(Protocol):
    header: ResponseHeader


class AuthRoleAddRequest(Protocol):
    def __init__(self, name: str):
        ...


class AuthRoleAddResponse(Protocol):
    header: ResponseHeader


class AuthRoleGetRequest(Protocol):
    def __init__(self, role: str):
        ...


class AuthRoleGetResponse(Protocol):
    header: ResponseHeader
    perm: typing.List[Permission]


class AuthRoleListRequest(Protocol):
    def __init__(self) -> None:
        ...


class AuthRoleListResponse(Protocol):
    header: ResponseHeader
    roles: typing.List[str]


class AuthRoleDeleteRequest(Protocol):
    def __init__(self, role: str):
        ...


class AuthRoleDeleteResponse(Protocol):
    header: ResponseHeader


class AuthRoleGrantPermissionRequest(Protocol):
    def __init__(self, name: str, perm: Permission):
        ...


class AuthRoleGrantPermissionResponse(Protocol):
    header: ResponseHeader


class AuthRoleRevokePermissionRequest(Protocol):
    def __init__(self, role: str, key: bytes, range_end: bytes):
        ...


class AuthRoleRevokePermissionResponse(Protocol):
    header: ResponseHeader


class AuthStub(Protocol):
    def __init__(self, channel: Channel):
        ...

    async def AuthEnable(
        self, request: AuthEnableRequest
    ) -> AuthEnableResponse:
        ...

    async def AuthDisable(
        self, request: AuthDisableRequest
    ) -> AuthDisableResponse:
        ...

    async def Authenticate(
        self, request: AuthenticateRequest
    ) -> AuthenticateResponse:
        ...

    async def UserAdd(
        self, request: AuthUserAddRequest
    ) -> AuthUserAddResponse:
        ...

    async def UserGet(
        self, request: AuthUserGetRequest
    ) -> AuthUserGetResponse:
        ...

    async def UserList(
        self, request: AuthUserListRequest
    ) -> AuthUserListResponse:
        ...

    async def UserDelete(
        self, request: AuthUserDeleteRequest
    ) -> AuthUserDeleteResponse:
        ...

    async def UserChangePassword(
        self, request: AuthUserChangePasswordRequest
    ) -> AuthUserChangePasswordResponse:
        ...

    async def UserGrantRole(
        self, request: AuthUserGrantRoleRequest
    ) -> AuthUserGrantRoleResponse:
        ...

    async def UserRevokeRole(
        self, request: AuthUserRevokeRoleRequest
    ) -> AuthUserRevokeRoleResponse:
        ...

    async def RoleAdd(
        self, request: AuthRoleAddRequest
    ) -> AuthRoleAddResponse:
        ...

    async def RoleGet(
        self, request: AuthRoleGetRequest
    ) -> AuthRoleGetResponse:
        ...

    async def RoleList(
        self, request: AuthRoleListRequest
    ) -> AuthRoleListResponse:
        ...

    async def RoleDelete(
        self, request: AuthRoleDeleteRequest
    ) -> AuthRoleDeleteResponse:
        ...

    async def RoleGrantPermission(
        self, request: AuthRoleGrantPermissionRequest
    ) -> AuthRoleGrantPermissionResponse:
        ...

    async def RoleRevokePermission(
        self, request: AuthRoleRevokePermissionRequest
    ) -> AuthRoleRevokePermissionResponse:
        ...
