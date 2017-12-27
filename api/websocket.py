import aiohttp
import asyncio
import time
from aiohttp import web
from app import App

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    session_id = request.match_info['session_id']
    if session_id not in App.sessions:
        return web.Response(status=404)

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

