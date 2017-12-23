import soundcloud
import os

client_id = os.environ.get('SOUNDCLOUD_CLIENT_ID')
soundcloud_client = soundcloud.Client(client_id=client_id)