import hashlib
import base64

def new_session_id():
    hash_input = 'plunkbat'.encode('utf-8')
    return base64.urlsafe_b64encode(hashlib.md5(hash_input).digest()).decode()[:10]
