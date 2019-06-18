"""The module contains etcd client for API V2."""
import asyncio
import typing
import json

from aiohttp import client, client_exceptions  # type: ignore
from aiohttp.client_reqrep import ClientResponse  # type: ignore

from . import models, exceptions


class Client:
    """V2 API client implementation."""

    PREFIX = 'v2'

    def __init__(
            self, host: str = 'localhost', port: int = 2379,
            protocol: str = 'http',
            ca_cert=None, cert_key=None, cert_cert=None, timeout=None,
            username: typing.Optional[str] = None,
            password: typing.Optional[str] = None,
            loop: typing.Optional[asyncio.AbstractEventLoop] = None
    ):
        """Initialize the etcd client."""
        self.host = host
        self.port = port
        self.protocol = protocol
        self.ca_cert = ca_cert
        self.cert_key = cert_key
        self.cert_cert = cert_cert
        self.timeout = timeout
        self.loop = loop or asyncio.get_event_loop()
        _auth = None
        if username and password:
            _auth = client.BasicAuth(
                login=username, password=password,
                encoding='utf-8'
            )
        elif username or password:
            raise ValueError(
                '`username` and `password` both must have a value or None'
            )
        self.inner_client = client.ClientSession(loop=self.loop, auth=_auth)
        self.kv = KV(self)

    async def version(self) -> models.VersionResponse:
        """Return etcd version response
        """
        version_url = '/'.join((self.uri, 'version'))
        resp = await self.inner_client.get(version_url)

        await _raise_for_status(resp, [200])
        return await _process_response(resp, models.VersionResponse)

    @property
    def uri(self) -> str:
        """Return base uri for etcd API.

        :return: base uri
        """
        return '{protocol}://{host}:{port}'.format(
            protocol=self.protocol, host=self.host, port=self.port
        )


class KV:
    """Key-Value API implementation."""

    PREFIX = 'keys'

    def __init__(self, client: Client):
        """Initialize the key-value API subsystem."""
        self.client = client

    def _get_url(self, key) -> str:
        return '/'.join(
            (self.client.uri, self.client.PREFIX, self.PREFIX, key)
        )

    async def get(self, key: str) -> models.GetResponse:
        """Get the key value from etcd.

        :raise: :py:class:`aioetcd.exceptions.HttpError` - Error during
                the HTTP-request
        :raise: :py:class:`aioetcd.exceptions.ParseError` - Unexpected
                response received from the etcd
        :raise: :py:class:`aioetcd.exceptions.EtcdError` - Etcd managed
                error, for example `Key not found`
        """
        resp = await self.client.inner_client.get(self._get_url(key))
        await _raise_for_status(resp, [200])
        return await _process_response(resp, models.GetResponse)

    async def set(
            self,
            key: str,
            value: str,
            ttl=None,
            refresh=None,
            prev_exist=None
    ) -> models.SetResponse:
        """Set the value of the ``key`` or updates it if the ``key`` already
        exists.
        """
        resp = await self.client.inner_client.put(
            self._get_url(key), data={'value': value}
        )
        await _raise_for_status(resp, [200, 201])
        return await _process_response(resp, models.SetResponse)

    async def wait(self, key, wait_index=None):
        """Wait for changes in the ``key``."""
        pass

    async def post(self, key, value):
        """Put the new value to the ``key`` directory."""
        pass

    async def get_dir(self, key):
        pass

    async def delete(self, key):
        _ = await self.client.inner_client.delete(self._get_url(key))


T = typing.TypeVar(
    'T', models.EtcdResponse, models.GetResponse, models.VersionResponse,
    models.SetResponse
)


async def _raise_for_status(
        response: ClientResponse,
        expected_codes: typing.Iterable[int] = (200,)
):
    if response.status not in expected_codes:
        try:
            data = await response.json()
            error = models.ErrorResponse.from_dict(data)
        except client_exceptions.ContentTypeError:
            raise exceptions.HttpError(
                'Error during request. Response code: {}, '
                'reason: {}'.format(
                    response.status, await response.text()
                )
            )
        except (json.JSONDecodeError, TypeError, KeyError) as ex:
            raise exceptions.ParseError(
                'Cannot parse the response: {}. '
                'Original error is: {}'.format(
                    await response.text(), ex
                )
            )
        raise exceptions.EtcdError(error.message, error_response=error)


async def _process_response(
        response: ClientResponse,
        model: typing.Type[T]
) -> T:
    try:
        payload = await response.json()
        return model.from_dict(payload)
    except (
        client_exceptions.ContentTypeError, json.JSONDecodeError,
        TypeError, KeyError
    ) as ex:
        raise exceptions.ParseError(
            'Cannot parse the response: {}. Original error is: {}'.format(
                await response.text(), ex
            )
        )
