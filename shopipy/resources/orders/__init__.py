from datetime import datetime
from shopipy.base import BaseClient
from .schemas import ShopifyOrders

class Orders(BaseClient):
    orders_path = "/orders"

    def __init__(self, *args, **kwargs):
        super(Orders, self).__init__(*args, **kwargs)

    def count(self, status: str = "any"):
        count_path = self.orders_path + "/count.json"
        return self._get(path=count_path, status=status)

    def find(self, order_id: str):
        find_path = self.orders_path + f"/{order_id}.json"
        return self._get(path=find_path)

    def get(
        self,
        attribution_app_id: str = None,
        created_at_max: datetime = None,
        created_at_min: datetime = None,
        fields: str = None,
        financial_status: str = None,
        fulfillment_status: str = None,
        ids: str = None,
        limit: int = 250,
        processed_at_max: datetime = None,
        processed_at_min: datetime = None,
        since_id: int = None,
        status: str = "any",
        updated_at_max: datetime = None,
        updated_at_min: datetime = None
    ):
        params = dict(
            attribution_app_id=attribution_app_id,
            created_at_max=created_at_max,
            created_at_min=created_at_min,
            fields=fields,
            financial_status=financial_status,
            fulfillment_status=fulfillment_status,
            ids=ids,
            limit=limit,
            processed_at_max=processed_at_max,
            processed_at_min=processed_at_min,
            since_id=since_id,
            status=status,
            updated_at_max=updated_at_max,
            updated_at_min=updated_at_min
        )
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.orders_path}.json", **cleaned)

    def get_all(self, serialize: bool = False):
        all_orders = []
        last_id = 0
        while True:
            try:
                response = self.get(limit=250, since_id=last_id)
            except Exception as error:
                print(str(error))
                continue
            
            if len(response['orders']) == 0:
                break
            
            if serialize:
                schemas = [ShopifyOrders(**single_order) for single_order in response['orders']]
                all_orders.extend(schemas)
                last_id = response['orders'][len(response['orders']) - 1].id # type: ignore
            
            else:
                all_orders.extend(response['orders'])
                last_id = response['orders'][len(response['orders']) - 1]['id']
            
        return all_orders