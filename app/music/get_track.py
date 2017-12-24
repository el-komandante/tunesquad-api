import asyncio
import functools
from clients.soundcloud_api import soundcloud_client

async def get_track(track_id):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, functools.partial(soundcloud_client.get, f'/tracks/{track_id}'))
    return await future