from __future__ import annotations
from typing_extensions import Protocol

from grpc.aio._channel import Channel  # type: ignore

from .common import ResponseHeader


class UserAddOptions(Protocol):
    no_password: bool

    def __init__(self, no_password: bool):
        ...


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
    def __init__(self, name: str, password: str, options: UserAddOptions):
        ...


class AuthUserAddResponse(Protocol):
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

    # async def UserGet(
    #   self, request: AuthUserGetRequest
    # ) -> AuthUserGetResponse:
    #     ...

    # async def UserList(
    #   self, request: AuthUserListRequest
    # ) -> AuthUserListResponse:
    #     ...

    # async def UserDelete(
    #   self, request: AuthUserDeleteRequest
    # ) -> AuthUserDeleteResponse:
    #     ...

    # async def UserChangePassword(
    #   self, request: AuthUserChangePasswordRequest
    # ) -> AuthUserChangePasswordResponse:
    #     ...

    # async def UserGrantRole(
    #   self, request: AuthUserGrantRoleRequest
    # ) -> AuthUserGrantRoleResponse:
    #     ...

    # async def UserRevokeRole(
    #   self, request: AuthUserRevokeRoleRequest
    # ) -> AuthUserRevokeRoleResponse:
    #     ...

    # async def RoleAdd(
    #   self, request: AuthRoleAddRequest
    # ) -> AuthRoleAddResponse:
    #     ...

    # async def RoleGet(
    #   self, request: AuthRoleGetRequest
    # ) -> AuthRoleGetResponse:
    #     ...

    # async def RoleList(
    #   self, request: AuthRoleListRequest
    # ) -> AuthRoleListResponse:
    #     ...

    # async def RoleDelete(
    #   self, request: AuthRoleDeleteRequest
    # ) -> AuthRoleDeleteResponse:
    #     ...

    # async def RoleGrantPermission(
    #   self, request: AuthRoleGrantPermissionRequest
    # ) -> AuthRoleGrantPermissionResponse:
    #     ...

    # async def RoleRevokePermission(
    #   self, request: AuthRoleRevokePermissionRequest
    # ) -> AuthRoleRevokePermissionResponse:
    #     ...
