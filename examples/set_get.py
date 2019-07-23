import asyncio

from aioetcd import client, exceptions


async def main():
    c = client.Client()
    set_result = await c.kv.set("key", "value")
    print("set response:", set_result)
    print("headers:", set_result.headers)
    assert set_result.node.key == "/key"
    assert set_result.node.value == "value"
    get_result = await c.kv.get("key")
    print("set response:", get_result)
    print("headers:", get_result.headers)
    assert get_result.node.key == "/key"
    assert get_result.node.value == "value"
    assert get_result.node.modified_index == set_result.node.modified_index
    assert get_result.node.created_index == set_result.node.created_index
    try:
        await c.kv.get("unknown_key")
    except exceptions.EtcdError as ex:
        print(ex, ex.error_response)
    else:
        raise RuntimeError("Exception did not raised")
    finally:
        await c.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
