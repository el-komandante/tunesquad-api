
from aiohttp import web
from .search import search_handler

app = web.Application()

app.router.add_get('/search', search_handler)