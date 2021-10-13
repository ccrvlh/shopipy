from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class HarmonizedCode(BaseModel):
    country_code: str
    harmonized_system_code: str


class InventoryItem(BaseModel):
    cost: str
    country_code_of_origin: str
    country_harmonized_system_codes: Optional[List[Optional[HarmonizedCode]]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    harmonized_system_code: Optional[int]
    id: Optional[int]
    harmonized_system_code: Optional[int]
    province_code_of_origin: Optional[str]
    sku: Optional[str]
    tracked: Optional[bool]
    requires_shipping: Optional[bool]


class InventoryLevel(BaseModel):
    inventory_item_id: Optional[int]
    available: Optional[int]
    location_id: Optional[int]
    updated_at: Optional[datetime]


class InventoryLocation(BaseModel):  
    active: Optional[bool]
    id: Optional[int]
    legacy: Optional[bool]
    updated_at: Optional[datetime]
    created_at: Optional[datetime]
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    country_code: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    province: Optional[str]
    province_code: Optional[str]
    zip: Optional[str]
    localized_country_name: Optional[str]
    localized_province_name: Optional[str]