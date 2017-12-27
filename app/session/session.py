from datetime import datetime
from queue import Queue

class Session():
    def __init__(self):
        self.queue = Queue()
        self.users = {}
        self.created_at = datetime.now()
            
    def add_user(self, nickname,conn):   
        if nickname in self.users:
            raise Exception(f'User with nickname {nickname} already exists.')
        else:
            self.users[nickname] = User(nickname, conn)

    async def play_music():
        async for song in self.queue:
            current_song = self.queue.deque
            duration = current_song.duration
            for user in self.users:
                user.conn.send_str(current_song.url)
            time.sleep(duration/1000) #divide by 1000 bc duration comes in ms