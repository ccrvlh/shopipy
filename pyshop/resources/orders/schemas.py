from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from pyshop.resources.fulfillment.schemas import Fulfillments # type: ignore
from pyshop.resources.transactions.schemas import Transactions # type: ignore
from pyshop.resources.customers.schemas import Address, CustomerShopify # type: ignore
from pyshop.resources.common.schemas import ShopMoney, AmountSet


class OrderAdjustments(BaseModel):
    id: Optional[str]
    order_id: Optional[str]
    refund_id: Optional[str]
    amount: Optional[str]
    tax_amount: Optional[str]
    kind: Optional[str]
    reason: Optional[str]
    amount_set: AmountSet
    tax_amount_set: AmountSet


class DiscountApplications(BaseModel):
    type: Optional[str]
    value: Optional[str]
    value_type: Optional[str]
    allocation_method: Optional[str]
    target_selection: Optional[str]
    target_type: Optional[str]
    description: Optional[str]
    title: Optional[str]


class DiscountCodes(BaseModel):
    code: Optional[str]
    amount: Optional[str]
    type: Optional[str]


class Properties(BaseModel):
    key: Optional[str]
    value: Optional[str]


class TaxLines(BaseModel):
    price: Optional[str]
    rate: Optional[str]
    title: Optional[str]


class DiscountAllocations(BaseModel):

    amount: Optional[str]
    disc_app_index: Optional[str]
    amount_set: Optional[AmountSet]


class LineItems(BaseModel):

    id: Optional[str]
    variant_id: Optional[str]
    title: Optional[str]
    quantity: Optional[str]
    sku: Optional[str]
    variant_title: Optional[str]
    vendor: Optional[str]
    fulfillment_service: Optional[str]
    product_id: Optional[str]
    requires_shipping: Optional[str]
    taxable: Optional[str]
    gift_card: Optional[str]
    name: Optional[str]
    variant_inventory_management: Optional[str]
    properties: Optional[List[Properties]]
    product_exists: Optional[str]
    fulfillable_quantity: Optional[str]
    grams: Optional[str]
    price: Optional[str]
    total_discount: Optional[str]
    fulfillment_status: Optional[str]
    price_set: Optional[AmountSet]
    total_discount_set: Optional[AmountSet]
    discount_allocations: Optional[List[DiscountAllocations]]
    tax_lines: Optional[List[TaxLines]]



class ShippingLine(BaseModel):
    id: Optional[str]
    title: Optional[str]
    price: Optional[str]
    code: Optional[str]
    source: Optional[str]
    phone: Optional[str]
    requested_fulfillment_service_id: Optional[str]
    delivery_category: Optional[str]
    carrier_identifier: Optional[str]
    discounted_price: Optional[str]
    price_set: Optional[AmountSet]
    discounted_price_set: Optional[AmountSet]
    discount_allocations: Optional[List[DiscountAllocations]]
    tax_lines: Optional[TaxLines]


class RefundItem(BaseModel):
    id: Optional[int]
    line_item: Optional[LineItems]
    line_item_id: Optional[int]
    quantity: Optional[int]
    restock_type: Optional[str]
    location_id: Optional[int]
    subtotal: Optional[float]
    total_tax: Optional[float]
    subtotal_set: Optional[AmountSet]
    total_tax_set: Optional[AmountSet]


class Refunds(BaseModel):
    id: Optional[str]
    order_id: Optional[str]
    created_at: Optional[datetime]
    note: Optional[str]
    user_id: Optional[str]
    processed_at: Optional[str]
    refund_line_items: Optional[List[Optional[RefundItem]]]
    transactions: Optional[List[Optional[Transactions]]]
    order_adjustments: Optional[Optional[List[OrderAdjustments]]]


class ShopifyOrders(BaseModel):

    id: Optional[int]
    email: Optional[str]
    closed_at: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[str]
    number: Optional[str]
    note: Optional[str]
    token: Optional[str]
    gateway: Optional[str]
    test: Optional[str]
    total_price: Optional[str]
    subtotal_price: Optional[str]
    total_weight: Optional[str]
    total_tax: Optional[str]
    taxes_included: Optional[str]
    currency: Optional[str]
    financial_status: Optional[str]
    confirmed: Optional[str]
    total_discounts: Optional[str]
    total_line_items_price: Optional[str]
    cart_token: Optional[str]
    buyer_accepts_marketing: Optional[str]
    name: Optional[str]
    referring_site: Optional[str]
    landing_site: Optional[str]
    cancelled_at: Optional[str]
    cancel_reason: Optional[str]
    total_price_usd: Optional[str]
    checkout_token: Optional[str]
    reference: Optional[str]
    user_id: Optional[str]
    location_id: Optional[str]
    source_identifier: Optional[str]
    source_url: Optional[str]
    processed_at: Optional[str]
    device_id: Optional[str]
    phone: Optional[str]
    customer_locale: Optional[str]
    app_id: Optional[str]
    browser_ip: Optional[str]
    landing_site_ref: Optional[str]
    order_number: Optional[str]
    discount_applications: Optional[List[DiscountApplications]]
    discount_codes: Optional[List[DiscountCodes]]
    note_attributes: Optional[List[Properties]]
    payment_gateway_names: Optional[List[Optional[str]]]
    processing_method: Optional[str]
    checkout_id: Optional[str]
    source_name: Optional[str]
    fulfillment_status: Optional[str]
    tax_lines: Optional[List[TaxLines]]
    tags: Optional[str]
    contact_email: Optional[str]
    order_status_url: Optional[str]
    presentment_currency: Optional[str]
    total_line_items_price_set: Optional[AmountSet]
    total_discounts_set: Optional[AmountSet]
    total_shipping_price_set: Optional[AmountSet]
    subtotal_price_set: Optional[AmountSet]
    total_price_set: Optional[AmountSet]
    total_tax_set: Optional[AmountSet]
    total_tip_received: Optional[str]
    line_items: Optional[List[LineItems]]
    shipping_lines: Optional[List[ShippingLine]]
    billing_address: Optional[Address]
    shipping_address: Optional[Address]
    fulfillments: Optional[List[Fulfillments]]
    refunds: Optional[List[Refunds]]
    customer: Optional[CustomerShopify]
    admin_graphql_api_id: Optional[str]

