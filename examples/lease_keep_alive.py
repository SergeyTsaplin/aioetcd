import asyncio
from aioetcd.client import Client


counter = 0


async def keep_alive_callback(response):
    print(response)


async def main(loop: asyncio.AbstractEventLoop):
    client = Client(
        endpoint="localhost:2379", username="root", password="root"
    )
    async with client.lease.keep_alive_context(ttl=10) as lease:
        print("lease:", lease)
        print("leases:", await client.lease.leases())
        await asyncio.sleep(10)
        print("awaken")
        print("leases:", await client.lease.leases())
    print("leases:", await client.lease.leases())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main(loop))
