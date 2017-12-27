import aiohttp
import asyncio
import time
from aiohttp import web
from app.app import TuneSquad

async def websocket_handler(request):
    print("in handler)")
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("next1")
    session_id = request.match_info['session_id']
    if session_id not in TuneSquad.sessions:
        return web.Response(status=404)


    if request.body_exists is False:
        return web.Response(status=400)
    
    body = await request.json()
    nickname = body.get('nickname')
    
    if session_id not in TuneSquad.sessions:
        return web.Response(status=404)
    elif nickname in TuneSquad.sessions[session_id].users:
        return web.Response(status=409)
    else:
        TuneSquad.sessions[session_id].new_user(nickname)
        return web.Response(
            status=200
        )
    print("next2")
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

