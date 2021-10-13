from datetime import datetime
from pyshopify.base import BaseClient

class Auth(BaseClient):
    def __init__(self, *args, **kwargs):
        super(Auth, self).__init__(*args, **kwargs)

    def create_permission_url(self):
        raise NotImplementedError

    def request_token(self):
        raise NotImplementedError
