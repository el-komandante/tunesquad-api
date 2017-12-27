import json
from app.app import TuneSquad
from aiohttp import web
from app.music.get_track import get_track

async def queue_handler(req):
    session_id = req.match_info['session_id']

    if session_id not in TuneSquad.sessions:
        return web.Response(status=404)
    
    body = await req.json()
    nickname = body.get('nickname')
    track_id = body.get('track_id')

    track = await get_track(track_id)

    stream = {
        'nickname': nickname,
        'title': track.title,
        'user': track.user,
        'artwork_url': track.artwork_url,
        'duration': track.duration,
        'url': track.stream_url
    }
    if TuneSquad.sessions[session_id].queue.empty():
        TuneSquad.sessions[session_id].queue.put_nowait(stream)
        TuneSquad.sessions[session_id].play_music()
    else:
        TuneSquad.sessions[session_id].queue.put_nowait(stream)

    return web.Response(status=200)
