from __future__ import annotations
from typing_extensions import Protocol

from grpc.aio._channel import Channel  # type: ignore

from aioetcd._rpc import rpc_pb2


class AuthStub(Protocol):
    def __init__(self, channel: Channel):
        ...

    async def AuthEnable(
        self, request: rpc_pb2.AuthEnableRequest
    ) -> rpc_pb2.AuthEnableResponse:
        ...

    async def AuthDisable(
        self, request: rpc_pb2.AuthDisableRequest
    ) -> rpc_pb2.AuthDisableResponse:
        ...

    async def Authenticate(
        self, request: rpc_pb2.AuthenticateRequest
    ) -> rpc_pb2.AuthenticateResponse:
        ...

    async def UserAdd(
        self, request: rpc_pb2.AuthUserAddRequest
    ) -> rpc_pb2.AuthUserAddResponse:
        ...

    async def UserGet(
        self, request: rpc_pb2.AuthUserGetRequest
    ) -> rpc_pb2.AuthUserGetResponse:
        ...

    async def UserList(
        self, request: rpc_pb2.AuthUserListRequest
    ) -> rpc_pb2.AuthUserListResponse:
        ...

    async def UserDelete(
        self, request: rpc_pb2.AuthUserDeleteRequest
    ) -> rpc_pb2.AuthUserDeleteResponse:
        ...

    async def UserChangePassword(
        self, request: rpc_pb2.AuthUserChangePasswordRequest
    ) -> rpc_pb2.AuthUserChangePasswordResponse:
        ...

    async def UserGrantRole(
        self, request: rpc_pb2.AuthUserGrantRoleRequest
    ) -> rpc_pb2.AuthUserGrantRoleResponse:
        ...

    async def UserRevokeRole(
        self, request: rpc_pb2.AuthUserRevokeRoleRequest
    ) -> rpc_pb2.AuthUserRevokeRoleResponse:
        ...

    async def RoleAdd(
        self, request: rpc_pb2.AuthRoleAddRequest
    ) -> rpc_pb2.AuthRoleAddResponse:
        ...

    async def RoleGet(
        self, request: rpc_pb2.AuthRoleGetRequest
    ) -> rpc_pb2.AuthRoleGetResponse:
        ...

    async def RoleList(
        self, request: rpc_pb2.AuthRoleListRequest
    ) -> rpc_pb2.AuthRoleListResponse:
        ...

    async def RoleDelete(
        self, request: rpc_pb2.AuthRoleDeleteRequest
    ) -> rpc_pb2.AuthRoleDeleteResponse:
        ...

    async def RoleGrantPermission(
        self, request: rpc_pb2.AuthRoleGrantPermissionRequest
    ) -> rpc_pb2.AuthRoleGrantPermissionResponse:
        ...

    async def RoleRevokePermission(
        self, request: rpc_pb2.AuthRoleRevokePermissionRequest
    ) -> rpc_pb2.AuthRoleRevokePermissionResponse:
        ...
