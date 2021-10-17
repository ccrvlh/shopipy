from datetime import datetime
from shopipy.base import BaseClient

class Customers(BaseClient):
    customer_path = "/customers"

    def __init__(self, *args, **kwargs):
        super(Customers, self).__init__(*args, **kwargs)

    def get_all(
        self,
        created_at_max: str = None,
        created_at_min: str = None,
        fields: str = None,
        ids: str = None,
        limit: int = 250,
        since_id: int = 0,
        updated_at_max: str = None,
        updated_at_min: str = None,
        serialize: bool = True
    ):
        params = dict(
            created_at_max=created_at_max,
            created_at_min=created_at_min,
            fields=fields,
            ids=ids,
            limit=limit,
            since_id=since_id,
            updated_at_max=updated_at_max,
            updated_at_min=updated_at_min
        )
        count_path = self.customer_path + ".json"
        response = self._get(path=count_path, params=dict(**params))
        all_customers = response.json()
        response = all_customers
        if serialize:
            response = [Customers(**customer) for customer in all_customers]
        return all_customers

    def get_customer(self, customer_id: str, fields: str = None):
        full_path = self.customer_path + f"/{customer_id}.json"
        return self._get(path=full_path, params=dict(fields=fields))

    def get_customer_orders(self):
        item_level = self.customer_path + f".json"
        return self._get(path=item_level)

    def count(self):
        raise NotImplementedError("Customer Adjustment Not Implemented.")

    def search(self):
        raise NotImplementedError("Set Customer Level Not Implemented.")

    # Addresses
    def list_customer_addresses(self):
        raise NotImplementedError("Set Customer Level Not Implemented.")

    def get_customer_address(self):
        raise NotImplementedError("Set Customer Level Not Implemented.")

    def set_customer_address(self):
        raise NotImplementedError("Set Customer Level Not Implemented.")

    def set_customer_default_address(self):
        raise NotImplementedError("Set Customer Level Not Implemented.")

    def delete_customer_address(self):
        raise NotImplementedError("Set Customer Level Not Implemented.")

