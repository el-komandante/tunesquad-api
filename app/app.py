from .session.session import Session

class App():
    def __init__(self):
        self.sessions = {}
    def new_session(self, session_id):
        if session_id in self.sessions:
            raise Exception(f'Session with id {session_id} already exists')
        else:
            self.sessions[session_id] = Session()


TuneSquad = App()