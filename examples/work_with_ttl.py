import asyncio

from aioetcd import client, exceptions


async def main():
    c = client.Client()
    set_result = await c.kv.set("key", "value", ttl=100)
    print("set response:", set_result)
    print("headers:", set_result.headers)
    get_result = await c.kv.get("key")
    print("set response:", get_result)
    print("headers:", get_result.headers)
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
