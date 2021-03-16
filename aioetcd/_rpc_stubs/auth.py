from __future__ import annotations
from typing_extensions import Protocol

from .common import ResponseHeader


class AuthenticateResponseProto(Protocol):
    header: ResponseHeader
    token: str
