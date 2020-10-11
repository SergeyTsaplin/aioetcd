import asyncio
from aioetcd.client import Client

from aioetcd.kv import (
    Compare,
    CompareResult,
    CompareTarget,
    CompareTargetUnion,
)


CA_CERT = b"""
-----BEGIN CERTIFICATE-----
MIIB1TCCAXqgAwIBAgIURyh09F4lMEYAOcO1u1wHUZP21xkwCgYIKoZIzj0EAwIw
SDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1TYW4gRnJhbmNp
c2NvMRQwEgYDVQQDEwtleGFtcGxlLm5ldDAeFw0yMDEwMDUxNzU2MDBaFw0yNTEw
MDQxNzU2MDBaMEgxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMN
U2FuIEZyYW5jaXNjbzEUMBIGA1UEAxMLZXhhbXBsZS5uZXQwWTATBgcqhkjOPQIB
BggqhkjOPQMBBwNCAAR+7ebbTMbOL5bGdnvwrF7Y6rJCDptQmyP7mknyKDR0d8RZ
qLK05YRb/WFVqVo2DWAUQscGthunFy2yV6deaWs5o0IwQDAOBgNVHQ8BAf8EBAMC
AQYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUdNdlPEjliwWinvXHx3ax0i/h
excwCgYIKoZIzj0EAwIDSQAwRgIhAKZXFLajg8EmfYhkmQeos1cOAm+XGfbbq4/c
wNTWWedoAiEA0pU5UNsa1cSwADHI6WIbsimoSkbogkDq0QATw5OGypI=
-----END CERTIFICATE-----
"""


async def main():
    # client = Client(endpoint="localhost:2377", ssl=True, username="root", password="root", ca_cert=CA_CERT)
    # client = Client(
    #     endpoint="localhost:2379", username="root", password="root"
    # )
    client = Client(endpoint="localhost:2379")
    put_response = await client.kv.put(b"/test_key", value=b"test")
    print(put_response)
    range_response = await client.kv.range(b"/test_key", None)
    print(range_response)
    ## Transaction
    txn_response = await client.kv.txn(
        compare=[
            Compare(
                result=CompareResult.EQUAL,
                target=CompareTarget.CREATE,
                key=b"/test/txn",
                target_union=CompareTargetUnion(create_revision=0),
            )
        ],
        success=[
            client.kv.put(b"/test/txn/1", value=b"test"),
        ],
        failure=[
            client.kv.range(b"/test/txn/1"),
        ],
    )
    print(txn_response)
    print(
        id(txn_response.responses[0].response),
        id(txn_response.responses[0].response_put),
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
