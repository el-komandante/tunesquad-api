import aiohttp
import asyncio
import time
from aiohttp import web
from app.app import App

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    session_id = request.match_info['session_id']

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws 

async def start_music(session_id):
    my_session = App.sessions[session_id]
    async for song in my_session.queue:
        current_song = my_session.queue.deque
        duration = current_song.duration
        for user in my_session.users:
            user.conn.send_str(current_song.url)
        time.sleep(duration*1000)