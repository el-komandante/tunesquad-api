from aiohttp import web
from .search import search_handler
from .websocket import websocket_handler

app = web.Application()

app.router.add_get('/search', search_handler)
app.router.add_get('/ws', websocket_handler)
