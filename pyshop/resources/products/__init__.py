from datetime import datetime
from pyshop.base import BaseClient
from pyshop.resources.products.schemas import Product # type: ignore

class Products(BaseClient):
    product_path = "/products"

    def __init__(self, *args, **kwargs):
        super(Products, self).__init__(*args, **kwargs)

    def list_products(
        self,
        collection_id: str = None,
        created_at_max: datetime = None,
        created_at_min: datetime = None,
        fields: str = None,
        handle: str = None,
        ids: str = None,
        limit: int = 250,
        presentment_currencies: datetime = None,
        product_type: datetime = None,
        published_at_max: datetime = None,
        published_at_min: datetime = None,
        published_status: str = None,
        since_id: int = None,
        status: str = None,
        title: str = None,
        vendor: str = None,
        updated_at_max: datetime = None,
        updated_at_min: datetime = None,
    ):
        params = dict(
            collection_id=collection_id,
            created_at_max=created_at_max,
            created_at_min=created_at_min,
            fields=fields,
            handle=handle,
            ids=ids,
            limit=limit,
            presentment_currencies=presentment_currencies,
            product_type=product_type,
            published_at_max=published_at_max,
            published_at_min=published_at_min,
            published_status=published_status,
            since_id=since_id,
            status=status,
            title=title,
            vendor=vendor,
            updated_at_max=updated_at_max,
            updated_at_min=updated_at_min
        )
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.product_path}.json", **cleaned)

    def get(self, product_id: str, fields: str = None):
        params = dict(product_id=product_id, fields=fields)
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.product_path}/{product_id}.json", **cleaned)

    def count(
        self,
        collection_id: str = None,
        created_at_max: datetime = None,
        created_at_min: datetime = None,
        product_type: datetime = None,
        published_at_max: datetime = None,
        published_at_min: datetime = None,
        published_status: str = None,
        vendor: str = None,
        updated_at_max: datetime = None,
        updated_at_min: datetime = None,
    ):
        params = dict(
            collection_id=collection_id,
            created_at_max=created_at_max,
            created_at_min=created_at_min,
            product_type=product_type,
            published_at_max=published_at_max,
            published_at_min=published_at_min,
            published_status=published_status,
            vendor=vendor,
            updated_at_max=updated_at_max,
            updated_at_min=updated_at_min
        )
        cleaned = self._clean_params(params)
        return self._get(path=f"{self.product_path}/count.json", **cleaned)

    def save(self, product: Product):
        return self._post(path=f"{self.product_path}.json", payload=product)

    def update(self, product: Product):
        return self._put(path=f"{self.product_path}.json", payload=product)

    def delete(self, product_id: str):
        return self._delete(path=f"{self.product_path}/{product_id}.json")
