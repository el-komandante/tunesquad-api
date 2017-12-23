import asyncio
import json
from aiohttp import web
from app.music.search import search_soundcloud

async def search_handler(req):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }
    results = await search_soundcloud(req.url.query.get('q'))
    tracks = []
    for track in results:
        tracks.append({
            'title': track.title,
            'user': track.user,
            'track_id': track.id,
            'play_count': track.playback_count,
            'likes': track.favoritings_count,
            'genre': track.genre,
            'duration': track.duration,
            'artwork_url': track.artwork_url,
            'stream_url': track.stream_url,
            'waveform_url': track.waveform_url
        })
    return web.Response(
        status=200,
        body=json.dumps(tracks)
    )