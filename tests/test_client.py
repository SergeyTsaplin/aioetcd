import pytest  # type: ignore
from aioetcd import client


pytestmark = pytest.mark.asyncio


async def test_client_init(event_loop):
    cl = client.Client()
    assert cl.host == "localhost"
    assert isinstance(cl.kv, client.KV)
