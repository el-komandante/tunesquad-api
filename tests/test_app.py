import unittest
from app.app import App
from app.session.new_session_id import new_session_id

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = App()

    def test_new_session(self):
        session_id = new_session_id()
        self.app.new_session(session_id)

        self.assertTrue(session_id in self.app.sessions)
