from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from pyshopify.resources.common.schemas import AmountSet, TaxItem

class Shipping(BaseModel):
    code: Optional[str]
    discounted_price: Optional[str]
    discounted_price_set: Optional[str]
    price: Optional[str]
    price_set: Optional[AmountSet]
    source: Optional[str]
    title: Optional[str]
    tax_lines: List[Optional[TaxItem]]
    carrier_identifier: Optional[str]
    requested_fulfillment_service_id: Optional[str]
