from pydantic.main import BaseModel
from typing import List, Optional
from datetime import datetime


class Option(BaseModel):
    option1: Optional[str]
    option2: Optional[str]
    option3: Optional[str]


class Price(BaseModel):
    currency_code: Optional[str]
    amount: Optional[str]


class CompareAtPrice(Price):
    pass


class PresentmentPrices(BaseModel):
    price: Optional[Price]
    compare_at_price: Optional[CompareAtPrice]


class Options(BaseModel):
    id: Optional[str]
    product_id: Optional[str]
    name: Optional[str]
    position: Optional[str]
    values: Optional[str]


class Image(BaseModel):
    id: Optional[int]
    product_id: Optional[int]
    position: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    alt: Optional[str]
    width: Optional[int]
    height: Optional[int]
    src: Optional[str]
    variant_ids: Optional[int]
    admin_graphql_api_id: Optional[str]


class Variant(BaseModel):
    id: Optional[int]
    product_id: Optional[int]
    title: Optional[str]
    price: Optional[str]
    sku: Optional[str]
    position: Optional[int]
    inventory_policy: Optional[str]
    compare_at_price: Optional[str]
    fulfillment_service: Optional[str]
    inventory_management: Optional[str]
    option: Optional[Option]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    taxable: Optional[bool]
    barcode: Optional[str]
    grams: Optional[int]
    image_id: Optional[int]
    weight: Optional[int]
    weight_unit: Optional[str]
    inventory_item_id: Optional[int]
    inventory_quantity: Optional[int]
    inventory_quantity_adjustment: Optional[int]
    old_inventory_quantity: Optional[int]
    requires_shipping: Optional[bool]
    admin_graphql_api_id: Optional[str]
    presentment_prices: Optional[List[PresentmentPrices]]
    tax_code: Optional[str]


class Product:
    id: Optional[int]
    title: Optional[str]
    body_html: Optional[str]
    vendor: Optional[str]
    product_type: Optional[str]
    collection_id: Optional[str]
    created_at: Optional[datetime]
    handle: Optional[str]
    updated_at: Optional[datetime]
    published_at: Optional[datetime]
    template_suffix: Optional[str]
    tags: Optional[str]
    published_scope: Optional[str]
    admin_graphql_api_id: Optional[str]
    variants: Optional[List[Variant]]
    options: Optional[List[Optional[Option]]]
    images: Optional[List[Optional[Image]]]
    status: Optional[str]

