from datetime import datetime
from pyshop.base import BaseClient

class Fulfillment(BaseClient):
    fulfillment_path = "/fulfillment"

    def __init__(self, *args, **kwargs):
        super(Fulfillment, self).__init__(*args, **kwargs)

    def list_fulfillments(self):
        count_path = self.fulfillment_path + ".json"
        return self._get(path=count_path)

    def get_fulfillment(self, item_id: str = "any"):
        item_path = self.fulfillment_path + f"/{item_id}.json"
        return self._get(path=item_path)

    def get_fulfillment_orders(self):
        item_level = self.fulfillment_path + f".json"
        return self._get(path=item_level)

    def count_fulfillments(self):
        raise NotImplementedError("Fulfillment Adjustment Not Implemented.")

    def search_fulfillment(self):
        raise NotImplementedError("Set Fulfillment Level Not Implemented.")

    # Addresses
    def list_fulfillment_addresses(self):
        raise NotImplementedError("Set Fulfillment Level Not Implemented.")

    def get_fulfillment_address(self):
        raise NotImplementedError("Set Fulfillment Level Not Implemented.")

    def set_fulfillment_address(self):
        raise NotImplementedError("Set Fulfillment Level Not Implemented.")

    def set_fulfillment_default_address(self):
        raise NotImplementedError("Set Fulfillment Level Not Implemented.")

    def delete_fulfillment_address(self):
        raise NotImplementedError("Set Fulfillment Level Not Implemented.")

