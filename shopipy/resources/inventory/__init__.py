from typing import List
from shopipy.base import BaseClient
from .schemas import InventoryItem, InventoryLocation

class Inventory(BaseClient):
    inv_items = "/inventory_items"
    inv_levels = "/inventory_levels"
    inv_locations = "/locations"

    def __init__(self, *args, **kwargs):
        super(Inventory, self).__init__(*args, **kwargs)

    # Inventory Item
    def list_items(self, ids: List[str] = None, limit: int = 250):
        if not ids:
            raise Exception("IDs not found. You need to provide the items' id's to get the inventory level.")
        list_path= self.inv_items + ".json"
        parsed_ids = ",".join(ids)
        return self._get(path=list_path, ids=parsed_ids, limit=limit)

    def get_item(self, item_id: str):
        item_path = self.inv_items + f"/{item_id}.json"
        return self._get(path=item_path)

    def update_item(self, item_id: str, item_payload: InventoryItem):
        item_path = self.inv_items + f"/{item_id}.json"
        return self._put(path=item_path, payload=item_payload.dict())

    # Inventory Item Level
    def get_items_level(self):
        item_level = self.inv_levels + f".json"
        return self._get(path=item_level)

    def set_level(self, available: int, inventory_item_id: int, location_id: int, disconnect_if_necessary: bool = False):
        payload = dict(
            available=available,
            inventory_item_id=inventory_item_id,
            location_id=location_id,
            disconnect_if_necessary=disconnect_if_necessary
        )
        full_path = self.inv_levels + "/set.json"
        return self._post(path=full_path, payload=payload)

    def adjust_level(self, available_adjustment: int, inventory_item_id: int, location_id: int):
        payload = dict(
            available_adjustment=available_adjustment,
            inventory_item_id=inventory_item_id,
            location_id=location_id
        )
        full_path = self.inv_levels + "/adjust.json"
        return self._post(path=full_path, payload=payload)

    def delete_level(self, inventory_item_id: int, location_id: int):
        full_path = self.inv_levels + ".json"
        return self._delete(path=full_path, inventory_item_id=inventory_item_id, location_id=location_id)

    def connect_item(self, location_id: int, inventory_item_id: int, relocate_if_necessary: bool = False):
        payload = dict(
            location_id=location_id,
            inventory_item_id=inventory_item_id,
            relocate_if_necessary=relocate_if_necessary
        )
        full_path = self.inv_levels + "/connect.json"
        return self._post(path=full_path, payload=payload)

    # Inventory Locations
    def list_locations(self, serialize: bool = False):
        """
        List a Shop's locations.
        With the option to serialize the result using Pydantic schemas
        """
        results = self._get(path=f"{self.inv_locations}.json")
        locations_list = results.json()
        results = locations_list
        if serialize:
            results = [InventoryLocation(**location) for location in locations_list]
        return results

    def get_location(self, location_id: str):
        location_path = self.inv_locations + f"/{location_id}.json"
        return self._get(path=location_path)

    def get_location_levels(self, location_id: str):
        location_path = self.inv_locations + f"/{location_id}/inventory_levels.json"
        return self._get(path=location_path)

    def count_locations(self):
        location_path = self.inv_locations + f"/count.json"
        return self._get(path=location_path)