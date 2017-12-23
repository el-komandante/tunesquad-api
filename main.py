from aiohttp import web
from api import api

web.run_app(api.app)