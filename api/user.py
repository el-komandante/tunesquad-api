import json
from aiohttp import web
from app.app import App

async def user_handler(req):
    if req.body_exists == False:
        return web.Response(status=400)
    session_id = req.match_info['session_id']
    
    body = await req.json()
    nickname = body.get('nickname')
    
    if session_id not in App.sessions:
        return web.Response(status=404)
    elif nickname in App.sessions[session_id].users:
        return web.Response(status=409)
    else:
        App.sessions[session_id].new_user(nickname)
        return web.Response(
            status=200
        )