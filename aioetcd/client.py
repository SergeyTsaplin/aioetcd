"""The moule contains etcd client for API V2."""
import typing

from aiohttp import client  # type: ignore


class Client:
    """V2 API client implementation."""

    PREFIX = 'v2'

    def __init__(self, host: str = 'localhost', port: int = 2379,
                 protocol: str = 'http',
                 ca_cert=None, cert_key=None, cert_cert=None, timeout=None,
                 username=None, password=None):
        """Initialize the etcd client."""
        self.host = host
        self.port = port
        self.protocol = protocol
        self.ca_cert = ca_cert
        self.cert_key = cert_key
        self.cert_cert = cert_cert
        self.timeout = timeout

        self._auth_headers = None
        if username or password:
            self._auth_headers = {
                'Authorization': client.BasicAuth(
                    login=username, password=password, encoding='utf-8'
                ).encode()
            }

        self.kv = KV(self)

    @property
    def uri(self) -> str:
        """Return base uri for etcd API.

        :return: base uri
        """
        return '{protocol}://{host}:{port}'.format(
            protocol=self.protocol, host=self.host, port=self.port
        )

    @property
    def auth_headers(self) -> typing.Optional[typing.Dict[str, str]]:
        """Return auth headers.

        :return: auth headers or None
        """
        return self._auth_headers


class KV:
    """Kay-Value API implementation."""

    PREFIX = 'keys'

    def __init__(self, client):
        """Initialize the key-value API subsystem."""
        self.client = client

    def _get_url(self, key):
        return '/'.join(
            (self.client.uri, self.client.PREFIX, self.PREFIX, key)
        )

    async def get(self, key):
        """Get the key value from etcd."""
        async with client.ClientSession() as session:
            _ = await session.get(
                self._get_url(key), headers=self.client.auth_headers
            )

    async def set(self, key, value, ttl=None, refresh=None, prev_exist=None):
        """Set the value of the ``key`` or updates it if the ``key`` already
        exists.
        """
        async with client.ClientSession() as session:
            _ = await session.put(
                self._get_url(key), headers=self.client.auth_headers
            )

    async def wait(self, key, wait_index=None):
        """Wait for changes in the ``key``."""
        pass

    async def post(self, key, value):
        """Put the new value to the ``key`` directory."""
        pass

    async def get_dir(self, key):
        pass

    async def delete(self, key):
        async with client.ClientSession() as session:
            _ = await session.delete(
                self._get_url(key), headers=self.client.auth_headers
            )
