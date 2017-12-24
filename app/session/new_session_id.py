import hashlib
import base64
import random

def new_session_id():
    return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()[:10]
