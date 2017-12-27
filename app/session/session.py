from datetime import datetime
import time
from queue import Queue
from app.user.user import User

class Session():
    def __init__(self):
        self.queue = Queue()
        self.users = {}
        self.created_at = datetime.now()
            
    def add_user(self, nickname,conn):   
        if nickname in self.users:
            raise Exception(f'User with nickname {nickname} already exists.')
        else:
            new_user = User(nickname, conn)
            self.users[nickname] = new_user

    async def play_music(self):
        while True:
            current_song = self.queue.get
            duration = current_song.duration
            for user in self.users:
                user.conn.send_str(current_song.url)
            time.sleep(duration/1000) #divide by 1000 bc duration comes in ms