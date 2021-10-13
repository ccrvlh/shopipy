from datetime import datetime
from pyshopify.base import BaseClient

class Collections(BaseClient):
    collection_path = "/collection"

    def __init__(self, *args, **kwargs):
        super(Collections, self).__init__(*args, **kwargs)

    def list_collections(self):
        count_path = self.inv_items + ".json"
        return self._get(path=count_path)

    def get_collection(self, item_id: str = "any"):
        item_path = self.inv_items + f"/{item_id}.json"
        return self._get(path=item_path)

    def get_collection_orders(self):
        item_level = self.inv_levels + f".json"
        return self._get(path=item_level)

    def count_collections(self):
        raise NotImplementedError("Collections Adjustment Not Implemented.")

    def search_collection(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

    # Addresses
    def list_collection_addresses(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

    def get_collection_address(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

    def set_collection_address(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

    def set_collection_default_address(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

    def set_collection_default_address(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

    def delete_collection_address(self):
        raise NotImplementedError("Set Collections Level Not Implemented.")

