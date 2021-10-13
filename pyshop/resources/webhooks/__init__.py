from datetime import datetime
from pyshop.base import BaseClient

class Webhooks(BaseClient):
    webhooks_path = "/webhook"

    def __init__(self, *args, **kwargs):
        super(Webhooks, self).__init__(*args, **kwargs)

    def list_webhooks(self):
        raise NotImplementedError

    def get_webhook(self):
        raise NotImplementedError

    def set_webhook(self):
        raise NotImplementedError

    def update_webhook(self):
        raise NotImplementedError

    def remove_webhooks(self):
        raise NotImplementedError
