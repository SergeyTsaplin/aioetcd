# import pytest

# from pytest_aiohttp import loop

from aioetcd import client


def test_client_init():
    cl = client.Client()
    assert cl.host == 'localhost'
    assert isinstance(cl.kv, client.KV)
