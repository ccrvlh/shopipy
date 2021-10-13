from datetime import datetime
from shopipy.base import BaseClient

class Webhooks(BaseClient):
    webhooks_path = "/webhooks"

    def __init__(self, *args, **kwargs):
        super(Webhooks, self).__init__(*args, **kwargs)

    def get_webhooks(
        self,
        address: str = None,
        created_at_max: datetime = None,
        created_at_min: datetime = None,
        fields: str = None,
        limit: int = 250,
        since_id: int = None,
        topic: str = None,
        updated_at_max: datetime = None,
        updated_at_min: datetime = None
    ):
        params = dict(
            address=address,
            created_at_max=created_at_max,
            created_at_min=created_at_min,
            fields=fields,
            topic=topic,
            limit=limit,
            since_id=since_id,
            updated_at_max=updated_at_max,
            updated_at_min=updated_at_min
        )
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.webhooks_path}.json", **cleaned)

    def get_webhook(
        self,
        webhook_id: str = None,
        fields: str = None
    ):
        params = dict(
            webhook_id=webhook_id,
            fields=fields
        )
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.webhooks_path}.json", **cleaned)

    def count(
        self,
        address: str = None,
        topic: str = None
    ):
        params = dict(
            address=address,
            topic=topic
        )
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.webhooks_path}/count.json", **cleaned)

    def set_webhook(self):
        raise NotImplementedError

    def update_webhook(self):
        raise NotImplementedError

    def remove_webhooks(self):
        raise NotImplementedError
