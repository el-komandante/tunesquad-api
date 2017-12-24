import json
from aiohttp import web
from app.app import App
from app.session.new_session_id import new_session_id

async def sessions_handler(req):
    body = await req.json()
    nickname = body.get('nickname')

    session_id = new_session_id()
    
    App.new_session(session_id)
    App.sessions[session_id].new_user(nickname)

    res = json.dumps({'session_id': session_id})

    return web.Response(
        status=200,
        body=res
    )