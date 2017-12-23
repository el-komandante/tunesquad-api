import asyncio
import functools
from clients.soundcloud_api import soundcloud_client

async def search_soundcloud(query):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, functools.partial(soundcloud_client.get, '/tracks', q=query))
    return await future