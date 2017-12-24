from datetime import datetime
from queue import Queue

class Session():
    def __init__(self):
        self.queue = Queue()
        self.users = {}
        self.created_at = datetime.now()
            
    def new_user(self, nickname):
        pass
    #     if nickname in self.users:
    #         raise Exception(f'User with nickname {nickname} already exists.')
    #     else:
    #         self.users[nickname] = User(nickname)