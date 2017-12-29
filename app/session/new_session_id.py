import hashlib
import random

def new_session_id():
    '''Creates a session ID from a random SHA256 hash'''
    return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()[:10]
