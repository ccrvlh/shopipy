from datetime import datetime
from pyshop.base import BaseClient

class Collections(BaseClient):
    collection_path = "/collection"

    def __init__(self, *args, **kwargs):
        super(Collections, self).__init__(*args, **kwargs)

    def list_collections(self):
        raise NotImplementedError

    def get_collection(self, item_id: str = "any"):
        raise NotImplementedError

    def get_collection_products(self):
        raise NotImplementedError

    def count_collections(self):
        raise NotImplementedError

    def search_collection(self):
        raise NotImplementedError