from aiohttp import web
from .search import search_handler
from .session import sessions_handler
from .queue import queue_handler
from .user import user_handler
from .websocket import websocket_handler
from .cors import cors_factory

app = web.Application(middlewares=[cors_factory])

# app.router.add_options()
app.router.add_get('/search', search_handler)
app.router.add_post('/sessions', sessions_handler)
app.router.add_put('/sessions/{session_id}/queue', queue_handler)
app.router.add_get('/sessions/{session_id}/ws', websocket_handler)