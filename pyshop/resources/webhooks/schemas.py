from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Address(BaseModel):
    id: Optional[str]
    customer_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    company: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    province: Optional[str]
    country: Optional[str]
    zip: Optional[str]
    phone: Optional[str]
    name: Optional[str]
    province_code: Optional[str]
    country_code: Optional[str]
    country_name: Optional[str]
    default: Optional[str]


class CustomerShopify(BaseModel):
    id: Optional[int]
    email: Optional[str]
    accepts_marketing: Optional[str]
    created_at: datetime
    updated_at: datetime
    first_name: Optional[str]
    last_name: Optional[str]
    orders_count: Optional[int]
    state: Optional[str]
    total_spent: Optional[float]
    last_order_id: Optional[str]
    note: Optional[str]
    verified_email: Optional[bool]
    multipass_identifier: Optional[str]
    tax_exempt: Optional[str]
    phone: Optional[str]
    tags: Optional[str]
    last_order_name: Optional[str]
    currency: Optional[str]
    addresses: Optional[List[Optional[Address]]]
    accepts_marketing_updated_at: Optional[datetime]
    marketing_opt_in_level: Optional[str]
    tax_exemptions: Optional[List[Optional[str]]]
    admin_graphql_api_id: Optional[str]
