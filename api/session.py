import asyncio
import json
from aiohttp import web
from app.app import App
from app.session.new_session_id import new_session_id

def sessions_handler(req):
    session_id = new_session_id()

    App.new_session(session_id)
    # body = await req.json()
    body = json.dumps({'session_id': session_id})
    # body = json.loads(req.body)
    return web.Response(
        status=200,
        body=body
    )